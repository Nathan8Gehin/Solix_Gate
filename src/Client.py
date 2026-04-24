import os
import asyncio
import aiohttp
from pathlib import Path
from dotenv import load_dotenv
from api.api import AnkerSolixApi

root_dir = Path(__file__).resolve().parent.parent
load_dotenv(root_dir / ".env")

EMAIL = os.getenv("ANKER_MAIL", "").strip()
PASSWORD = os.getenv("ANKER_PASSWORD", "").strip()

async def main():
    headers = {
        "User-Agent": "AnkerSolix/3.1.0 (iPhone; iOS 17.4.1; Scale/3.00)",
        "Accept-Language": "fr-FR",
    }

    timeout = aiohttp.ClientTimeout(total=30)

    async with aiohttp.ClientSession(timeout=timeout, headers=headers) as session:
        api = AnkerSolixApi(EMAIL, PASSWORD, "")

        # Injection profonde de la session
        api._session = session
        if hasattr(api, 'apisession'):
            api.apisession._session = session

        print(f"Waiting before connecting for {EMAIL}...")
        await asyncio.sleep(2)

        try:
            if await api.async_authenticate():
                print("Login successful!")

                await api.update_sites()
                await api.update_site_details()

                print("\n--- LIVE DATA ---")

                if api.sites:
                    for s_id, site in api.sites.items():
                        name = site.get('site_info', {}).get('site_name', 'Site')
                        sb = site.get('solarbank_info', {})

                        solar = sb.get('total_photovoltaic_power', 0)
                        batt_raw = sb.get('total_battery_power', 0)

                        try:
                            val = float(batt_raw)
                            batt = val * 100 if val < 1.1 else val
                        except:
                            batt = 0

                        print(f"[{name}] Solar: {solar}W | Battery: {batt:.0f}%")
                else:
                    print("No sites found on this account.")
            else:
                print("Login failed")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
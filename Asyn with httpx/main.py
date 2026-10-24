import httpx
import asyncio


async def fetch(client, url):
    response = await client.get(url)
    response.raise_for_status()
    data = response.json()
    return data


async def main():
    async with httpx.AsyncClient(timeout=10) as client:
        results = await asyncio.gather(
            fetch(client, "https://jsonplaceholder.typicode.com/users"),
            fetch(client, "https://jsonplaceholder.typicode.com/posts"),
            return_exceptions=True
        )

        users = results[0]
        posts = results[1]

        if isinstance(users, Exception):
            print("Users request failed:", users)
            return

        if isinstance(posts, Exception):
            print("Posts request failed:", posts)
            return

        userid = int(input("Enter the User id: "))
        found = False

        for user in users:
            count = 0

            if user["id"] == userid:
                found = True

                for post in posts:
                    if user["id"] == post["userId"]:
                        count = count + 1

                print("User:", user["name"])
                print("Total posts:", count)

        if found == False:
            print("User not found")


asyncio.run(main())
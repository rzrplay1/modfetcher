import requests
def fetch_mod(slug, minecraft_version, loader):# modrinth
    project_response = requests.get(f"https://api.modrinth.com/v2/project/{slug}")
    if project_response.status_code == 200:
        project_id = project_response.json()["id"]
        print("Project ID:", project_id)
        version_response = requests.get(f"https://api.modrinth.com/v2/project/{project_id}/version")
        if version_response.status_code == 200:
            versions = version_response.json()
            desired_version = next(
                (v for v in versions if minecraft_version in v["game_versions"] and loader in v["loaders"]),
                None
            )
            if desired_version:
                print("Found version:", desired_version["version_number"])

                files = desired_version["files"]
                for file in files:
                    if file["primary"]:
                        download_url = file["url"]
                        return download_url
            else:
                return f"fail_No version found for the specified Minecraft version and loader. mod:{slug}"
        else:
            return f"fail_Failed to fetch version information. mod:{slug}"
    else:
        return f"fail_Failed to fetch project ID. mod:{slug}"
slug_list=[# a list of mod names to fetch
    'ad-astra',
    'additional-placements',
    'alexs-mobs',
    'born-in-chaos',
    'botarium',
    'citadel',
    'crossroads',
    'disenchanting',
    'essentials',
    'explorations',
    'explorify',
    'framework',
    'geckolib',
    'hopo-better-mineshaft',
    'hopo-better-ruined-portals',
    'hopo-better-underwater-ruins',
    'iron-chests',
    'iron-furnaces',
    'jei',
    'koblods',
    'the-luminous-mod',
    'modern-life',
    'moonlight',
    'neat',
    'phenomena-structures',
    'playeranimator',
    'redeco',
    'redstonepen',
    'resourceful-config',
    'resourceful-lib',
    'silent-gear',
    'silent-lib',
    'sleep-tight',
    'special-drops',
    'the-undergarden',
    'vavs'
]
for mod in slug_list:
    a=fetch_mod(mod,'1.20.1','forge')
    b=a
    if a[:4]=='fail':b=f'\n{b}\n'
    print(b)
    if not a[:4]=='fail':
        with open(f'output/{a[a.find('/versions/')+19:]}', 'wb') as file:
            file.write(requests.get(a).content)
    open("output/log.txt", 'a', encoding='utf-8').write(b+'\n')
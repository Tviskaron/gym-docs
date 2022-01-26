import sys
sys.path.append("..")
menu = ["API", "Environment Creation", "Wrappers"]
# menu = ["Spaces", "Third Party Environments"]


ret = "#AUTOGENERATED: EDIT gen_menus in _scripts\n"
for item in menu:
    if item != "environment":
        link = item.replace(" ", "_").lower()
        file = open(f"../pages/{link}/index.md", "r")
        text = file.read()
        splits = text.split("##")
        headers = []
        for chunk in splits:
            header = chunk.split("\n")[0].replace("#", "", 1).strip()
            headers.append(header)
        
        headers = headers[1:]

        ret+= f"- title: {item}\n"
        link = item.replace(" ", "_").lower()
        ret+= f"  path: /{link}\n"
        if len(headers) > 0:
            ret+= "  sublinks: \n"
            for header in headers:
                ret+= f"    - title: \"{header}\"\n"
                link = header.replace(" ", "-").lower()
                ret+= f"      path: \"#{link}\"\n"

        ret+= "\n"
    else:
        pass

ret+= "#AUTOGENERATION ENDED"

print(ret)
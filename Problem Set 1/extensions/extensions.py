file = input("File:").lower().strip()
extensions_and_mimes = {
    ".gif":"image/gif",
    ".png":"image/png",
    ".jpg":"image/jpeg",
    ".jpeg":"image/jpeg",
    ".pdf":"application/pdf",
    ".zip":"application/zip",
    ".txt":"text/plain"}

extension = "." + file.split(".")[-1]
if extension in extensions_and_mimes:
    print(extensions_and_mimes[extension])
else:
    print("application/octet-stream")

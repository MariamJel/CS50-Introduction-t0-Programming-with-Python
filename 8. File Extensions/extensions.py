fileName = input("File name: ").strip().lower()
extension = fileName.split(".")[-1]
match extension:
    case "gif" | "jpeg" | "png":
        extension ="image/" + extension
    case "jpg":
        extension = "image/" + "jpeg"
    case "txt":
        extension = "text/plain"
    case "pdf" | "zip":
        extension = "application/" + extension
    case _:
        extension = "application/octet-stream"
print(extension)

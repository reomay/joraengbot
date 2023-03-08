import json
import shutil
import os


def Read(Path=None):
    if Path is None:
        raise RequirePath
    else:
        with open(Path, 'r', encoding="UTF-8") as File:
            jsonData = json.load(fp=File)
            return jsonData


def Write(Path=None, Object=None):
    if Path is None:
        raise RequirePath
    if Object == {}:
        pass
    elif Object is None:
        raise RequireObject
        os.makedirs()

    path, filename = os.path.split(Path)

    os.makedirs(path, exist_ok=True)
    with open(Path, 'w', encoding="UTF-8") as File:
        json.dump(fp=File, obj=Object, indent=4)


def Update(Path: str = None, Object=None):
    if Path is None:
        raise RequirePath
    elif Object is None:
        raise RequireObject
    else:
        tempdata = json.load(fp=open(Path, 'r', encoding="UTF-8"))
        tempdata.update(Object)
        json.dump(fp=open(Path, 'w', encoding="UTF-8"), obj=tempdata, indent=4)


def BackupWrite(Path=None, Object=None) -> str:
    if Path is None:
        raise RequirePath
    if Object == {}:
        pass
    elif Object is None:
        raise RequireObject
    originalFileName = str(Path).split('.')
    backupFileName = originalFileName[0] + "_backup" + originalFileName[1]
    shutil.copyfile(src=Path, dst=backupFileName)
    result = 0
    try:
        with open(Path, 'w', encoding="UTF-8") as File:
            json.dump(fp=File, obj=Object, indent=4)
        result = "success"
    except json.JSONDecodeError:
        with open(backupFileName, 'r', encoding="UTF-8") as File:
            Data = File.read()
            with open(Path, 'r', encoding="UTF-8") as File:
                json.dump(fp=File, obj=Data, indent=4)
            result = f"JSONDecodeError\n\n{json.JSONDecodeError.msg}"
    except Exception as Error:
        result = Error
    finally:
        os.remove(path=backupFileName)
        return result


class SimpleJSONExceptions(Exception): pass
class RequirePath(SimpleJSONExceptions): pass
class RequireObject(SimpleJSONExceptions): pass
import os, os.path, pathlib, shutil

class Directory:
    @classmethod
    def Create(cls, path): pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    @classmethod
    def Copy(cls, src, dst): return shutil.copytree(src, dst)
    @classmethod
    def Delete(cls, path): shutil.rmtree(path)
    @classmethod
    def Move(cls, src, dst): return shutil.move(src, dst)a

    @classmethod
    def GetSize(cls, path): return shutil.disk_usage(path)

    @classmethod
    def Which(cls, command): return shutil.which(command)

    @classmethod
    def Archive(cls, src, dst):
        ext = os.path.splitext(dst)[1:]
        archive_exts = [f[0] for f in shutil.get_archive_formats()]
        if ext not in archive_exts : raise Exception('アーカイブ拡張子は次のいずれかのみ可能です。{}'.format(archive_exts))
        return shutil.make_archive(os.path.dirname(dst), ext, root_dir=src, base_dir=src)

    def UnArchive(cls, src, dst=None):
        shutil.unpack_archive(src, dst)


import os, os.path, pathlib, shutil

class Directory:
    @classmethod
    def IsExist(cls, path): return os.path.isdir(path)
    @classmethod
    def Create(cls, path): os.makedirs(path, exist_ok=True)
    @classmethod
    def Copy(cls, src, dst): return shutil.copytree(src, dst)
    @classmethod
    def Delete(cls, path): shutil.rmtree(path)
    @classmethod
    def Move(cls, src, dst): return shutil.move(src, dst)
    @classmethod
    def Archive(cls, src, dst):
        ext = os.path.splitext(dst)[1][1:]
        archive_exts = [f[0] for f in shutil.get_archive_formats()]
        if ext not in archive_exts : raise Exception('拡張子\'{}\'は不正値です。アーカイブ拡張子は次のいずれかのみ可能です。{}'.format(ext, archive_exts))
        head, tail = os.path.split(src)
        base_name = os.path.join(os.path.dirname(dst), tail)
        root_dir = os.path.join(os.path.dirname(dst), head)
        base_dir = tail
        return shutil.make_archive(base_name, ext, root_dir=root_dir, base_dir=base_dir)

    @classmethod
    def UnArchive(cls, src, dst=None):
        shutil.unpack_archive(src, dst)
     
    """
    @classmethod
    def SetCurrentWorkingDirectory(cls, path):
        if os.path.isdir(): os.chdir(path)
    @classmethod
    def GetCurrentWorkingDirectory(cls):
        return os.getcwd()
    """

    """
    @classmethod
    def SetMode(cls, path, mode=0o755):
        # mode は3桁の8進数値か文字列
        pathlib.Path(path).chmod(mode)
    def GetMode(cls, path):
        return oct(os.stat(path).st_mode)
    @classmethod
    def GetModeName(cls, path):
        return stat.filemode(cls.GetMode(path))
    # -rwxrwxrwx
    @classmethod
    def SetModeName(cls, path, mode_name):
        mname = mode_name.strip()
        if mname.startswith('-'): mname = mname[1:]
        mode_names = [
            '---',
            '--x',
            '-w-',
            '-wx',
            'r--',
            'r-x',
            'rw-',
            'rwx'
        ]
        try:
            owner = [i for i, n in enumerate(node_names) if n == mname[0:3]][0]
            group = [i for i, n in enumerate(node_names) if n == mname[3:6]][0]
            other = [i for i, n in enumerate(node_names) if n == mname[6:9]][0]
            return oct(str(owner)+str(group)+str(other))
        except:
            import trackback
            trackback.print_exc()
            raise Exception('引数mode_nameは\'-rwxrwxrwx\'の書式で入力してください。owner, group, other, の順に次のパターンのいずれかを指定します。pattern={}。r,w,xはそれぞれ、読込、書込、実行の権限です。-は権限なしを意味します。'.format(mode_names))

    # epock
    @classmethod
    def GetModifiedDateTime(cls, path):
        return os.stat(path).st_mtime
        #return os.path.getmtime(path)

    @classmethod
    def SetModifiedDateTime(cls, path, mtime):
        os.utime(path, (os.stat(path).st_atime, mtime))

    @classmethod
    def GetAccessDateTime(cls, path):
        return os.stat(path).st_atime
        #return os.path.getatime(path)
    @classmethod
    def SetAccessDateTime(cls, path, atime):
        os.utime(path, (atime, os.stat(path).st_mtime))

    @classmethod
    def GetChangedMetaDataDateTime(cls, path):
        return os.stat(path).st_ctime
        #return os.path.getctime(path)
    @classmethod
    def GetCreateDateTime(cls, path):
        if 'posix' == os.name:
            return os.stat(path).st_birthtime
        elif 'nt' == os.name:
            return os.stat(path).st_ctime
        else:
            return os.stat(path).st_ctime
    """
    

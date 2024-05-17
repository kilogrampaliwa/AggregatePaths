

class aggre:

    def __init__(self, lines: list[str], banned: list[str] = [''], wanted: list[str] = [''], delete: list[str] = ['']):

        self.lines = lines
        self.__banned = False
        if banned != [''] : self.__banned = banned
        self.__wanted = False
        if wanted != [''] : self.__wanted = wanted
        self.__delete = False
        if delete != [''] : self.__delete = delete
        self.lines = self.__f_lines()
        self.one_line = self.__f_one_line()

    def __f_lines(self):

        def rm_nlines(lines: list[str]):
            new_lines = []
            for line in lines:
                if line[-1]=='\n':      new_lines.append(line[:-1])
                else:                   new_lines.append(line)
            return new_lines

        def del_banned(lines: list[str]):
            for banned_word in self.__banned:
                temp_lines = []
                for line in lines:
                    if banned_word not in line: temp_lines.append(line)
                lines = temp_lines
            return lines

        def add_wanted(lines: list[str]):
            out_list = []
            for wanted_word in self.__wanted:
                for line in lines:
                    if wanted_word in line and wanted_word not in out_list: out_list.append(line)
            return out_list

        def rmv_delete(lines: list[str]):
            for delete_word in self.__delete:
                temp_list = []
                for line in lines:
                    temp_list.append(line.replace(delete_word, ''))
                lines = temp_list
            return lines

        temporary = rm_nlines(self.lines)
        if self.__banned:   temporary = del_banned(temporary)
        if self.__wanted:   temporary = add_wanted(temporary)
        if self.__delete:   temporary = rmv_delete(temporary)

        return temporary

    def __f_one_line(self):
        all_in_line = ''
        for line in self.lines: all_in_line += line
        return all_in_line
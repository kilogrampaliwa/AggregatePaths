

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

        def del_banned(lines: list[str]):

            for banned_word in self.__banned:   out_list = [line for line in lines if banned_word not in line]
            return out_list

        def add_wanted(lines: list[str]):

            for wanted_word in self.__wanted:   out_list = [line for line in lines if wanted_word in line]
            return out_list

        def rmv_delete(lines: list[str]):

            for delete_word in self.__delete:   out_list = [line.replace(delete_word, '') for line in lines]
            return out_list

        temporary = self.lines
        if self.__banned:   temporary = del_banned(temporary)
        if self.__wanted:   temporary = add_wanted(temporary)
        if self.__delete:   temporary = rmv_delete(temporary)

        return temporary

    def __f_one_line(self): return [' ' + line for line in self.lines]
class Database():
    def __init__(self, data_filename="data_base.csv"):
        self.data_filename = data_filename
        self.data = []
        with open(self.data_filename, "r") as f:
            for line in f:
                self.data.append(line.strip())

    def __getitem__(self, index):
        return self.data[index]

    def _save(self):
        with open(self.data_filename, "w") as f:
            for data in self.data:
                f.write(data)
                f.write("\n")

    def add(self, new_user):
            self.data.append(','.join(new_user))
            self._save()

    def remove(self, user_name):
        for row in self.data:
            if user_name in row:
                self.data.remove(row)
                self._save()

    # def multiple_users(self, user_name):
    #     print("stuf")
    #     not_sameness = True
    #     for row in self.data:
    #         if user_name[0] in row:
    #             not_sameness = False
    #             return not_sameness
    #         return not_sameness

#c.add(['test', 'abcd', 'ddddd', '452k'])
# print(c[1][:8])

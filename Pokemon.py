class Pokemon:
    def __init__(self, dex, name, Stats, P_TYPE, S_TYPE,Tera_Type,Forms):
        self.dex = dex
        self.name = name
        self.HP = Stats["HP"]
        self.ATK = Stats["ATK"]
        self.DEF =  Stats["DEF"]
        self.SPATK = Stats["SPATK"]
        self.SPDEF = Stats["SPDEF"]
        self.SPEED = Stats["SPEED"]
        self.TYPE = [P_TYPE, S_TYPE]
        self.Health = Stats["HP"]
        self.Tera_Type = Tera_Type
        self.Level = 50
        self.Forms = Forms
        self.current_form = "Original"
        self.moves = []
        self.move_max = False
        self.move_gmax = False
    def activate_gimmick(self, form):
        self.move_max = True
        if form == "Gmax":
            self.move_gmax = True
    def activate_form(self, form):
        form_data = self.Forms[form]
        self.current_form = form
        if "Gmax" in form:
            self.ATK = form_data["ATK"]
            self.DEF = form_data["DEF"]
            self.SPATK = form_data["SPATK"]
            self.SPDEF = form_data["SPDEF"]
            self.SPEED = form_data["SPEED"]
            self.TYPE = [form_data["P-Type"],form_data["S-Type"]]
            self.activate_gimmick(form)
            ratio = self.Health / self.HP
            self.HP = form_data["HP"]
            self.Health = round(self.HP * ratio)
        elif "Dmax" in form:
            self.activate_gimmick(form)
            ratio = self.Health / self.HP
            self.HP *= 1.5
            self.HP = round(self.HP)
            self.Health = round(self.HP * ratio)
        elif "Mega" in form:
            self.HP = form_data["HP"]
            self.ATK = form_data["ATK"]
            self.DEF = form_data["DEF"]
            self.SPATK = form_data["SPATK"]
            self.SPDEF = form_data["SPDEF"]
            self.SPEED = form_data["SPEED"]
            self.TYPE = [form_data["P-Type"],form_data["S-Type"]]
    def calc_health(self, HP , level):
        pass
class Move:
    def __init__(self,name, type, category, power, accuracy, pp, priority, crit):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.max_pp = pp
        self.current_pp = pp
        self.priority = priority
        self.crit = crit
    def use_move(self):
        if self.current_pp > 0:
            self.current_pp -= 1
            return True
        elif self.current_pp == 0:
            print(f"{self.name} has no PP left!")
            return False
self.__score = 0
self.text = ["BLACK","PINK","GREEN","BLUE","YELLOW","RED"]
self.random_number_for_text = random.randint(0,5)
self.color = ["black","pink","green","blue","yellow","red"]
label_name["text"] = self.text[self.random_number_for_text]
label_name["fg"] = self.text[self.random_number_for_text]
btn = Button(root, text="START" , command=obj.updateGame, bg="dark olive green", fg="white", relief=FLAT, padx=10, pady=1, font =("Arial",15))


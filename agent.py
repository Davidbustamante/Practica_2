import random

class Agent(object):

    def __init__(self, inventory_size):
        self.consontants = "bcdfghjklmnpqrstvwxyz"
        self.vowels = "aeiou"
        self.inventory = [[] for _ in range(inventory_size)]

    def is_stable(self):
        total_names = 0
        for names in self.inventory:
            total_names += len(names)
        return total_names == len(self.inventory)

    def create_name(self, max_syllables):
        number_of_syllables = random.randint(1, max_syllables)
        new_name = ""
        for i in range(number_of_syllables):
            new_name += random.choice(self.consontants)
            new_name += random.choice(self.vowels)
        return new_name

    def agrees(self, k, name):
        return name in self.inventory[k]

    def add_name(self, k, name):
        # Only add if it's not in the inventory
        if not self.agrees(k, name):
            self.inventory[k].append(name)
            self.inventory[k].sort(key=len)

    def utter_to(self, hearer):
        # Choose random topic
        k = random.randint(0, len(self.inventory)-1)
        if len(self.inventory[k]) != 0:
            # Assume it's always sorted
            utterance = self.inventory[k][-1]
        else:
            # Create name if empty 
            utterance = self.name(k)

        # Communication
        is_agreement = hearer.agrees(k, utterance)
        if is_agreement:
            hearer.inventory[k] = [utterance]
            self.inventory[k] = [utterance]
        else:
            hearer.add_name(k, utterance)
        return utterance, is_agreement

    def name(self, k, max_syllables=8):
        new_name = self.create_name(max_syllables)
        self.add_name(k, new_name)
        return new_name
    
    def __str__(self):
        output = ""
        for k in range(len(self.inventory)):
            output += "Meaning %d: %s\n" % (k, str(self.inventory[k]))

        return output

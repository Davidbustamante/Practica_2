import sys
from statistics import mean
from agent import Agent, random

def main():
    if len(sys.argv) < 4:
        no_agents = int(input("Set number of agents: "))
        no_objects = int(input("Set number of meanings: "))
        max_iter = int(input("Set max iterations: "))
    else:
        no_agents = int(sys.argv[1])
        no_objects = int(sys.argv[2])
        max_iter = int(sys.argv[3])
    
    agent_set = set([Agent(no_objects) for _ in range(no_agents)])
    
    def all_known_names(agent_set):
        all_names = set()
        for agent in agent_set:
            for names in agent.inventory:
                all_names = all_names.union(set(names))
        return all_names
    
    def all_per_meaning_names(agent_set):
        all_names = [set() for _ in range(no_objects)]
        for agent in agent_set:
            for k in range(no_objects):
                all_names[k] = all_names[k].union(set(agent.inventory[k]))
        return all_names
    
    def context_is_stable(agent_set):
        all_names = all_per_meaning_names(agent_set)
        for names in all_names:
            if len(names) != 1:
                return False
        return True
    
    print("")
    i = 0
    while (max_iter < 0 or i < max_iter) and not context_is_stable(agent_set):
        # Take two at random
        talker, hearer = random.sample(agent_set, 2)
        name, is_agreement = talker.utter_to(hearer)
        
        # Print stats
        print("Iteration %d: %s (agreed? %s)" % (i, name, is_agreement))
        known_names = all_known_names(agent_set)
        print("Known names: %d (mean length: %.2f)" % (len(known_names),
            mean([len(name) for name in known_names])
            ))
        print("Known names per meaning:")
        names_per_meaning = all_per_meaning_names(agent_set)
        for k in range(no_objects):
            try:
                print("\tMeaning %d: %d (mean length: %.2f)" % (k, 
                    len(names_per_meaning[k]), 
                    mean([len(name) for name in names_per_meaning[k]])
                    ))
            except:
                print("\tMeaning %d: %d" % (k, len(names_per_meaning[k])))
        i += 1
    
    print("\nAgreed names:")
    for agent_id, agent in enumerate(agent_set):
        print("\n Agent %d: \n" % (agent_id + 1))
        print(str(agent))

if __name__ == "__main__":
    main()

import os
from itertools import combinations

### Code written during the GREEKC Malaga Hackathon
### The objective was to generate features to train a BERT model
### 

pairs_train_file = open("TFTG_gad/train.tsv", 'w')
pairs_dev_file = open("TFTG_gad/dev.tsv", "w")
pairs_test_file = open("TFTG_gad/test.tsv", "w")
pairs_test_file.write("index\tsentence\tlabel\n")
trainfiles = ['TFTG/' + f for f in os.listdir("TFTG/") if f.endswith('.txt')]
ip = 0
for it, t in enumerate(trainfiles):
    with open(t, 'r') as textfile:
         doctext = textfile.read()
         #print(doctext)
    all_entities = {}
    positive_relations = []
    with open(t.split(".")[0] + ".ann", 'r') as annfile:
         for a in annfile:
             if a.startswith("T"):
                 #print("entity", a)
                 values = a.strip().split()
                 start = int(values[2])
                 end = int(values[3])
                 #print(doctext[start:end])
                 all_entities[values[0]] = (start, end)
             elif a.startswith("R"):
                 values = a.strip().split()
                 positive_relations.append((values[2].split(":")[1], values[3].split(":")[1]))
    #print(len(all_entities), len(positive_relations))
     
    for pair in combinations(all_entities, 2):
        label = 0
        if pair in positive_relations:
            print(pair)
            label = 1
        e1 = all_entities[pair[0]]
        e2 = all_entities[pair[1]]
        if e1[0] > e2[0]:
            e1, e2 = e2, e1        
        #if e2[0] - e1[0] > 100:
        #    continue
        #print(e1, e2)
        masked_text = doctext[e1[0]-100:e1[0]] + "@GENE$" + doctext[e1[1]:e2[0]] + "@DISEASE$" + doctext[e2[1]:e2[1]+100]
        #print(masked_text)
        if it < 78:
            pairs_train_file.write(masked_text.replace("\n", "") + "\t" + str(label) + "\n")
        elif 78 < it < 104:
            pairs_dev_file.write(masked_text.replace("\n", "") + "\t" + str(label) + "\n")
        elif it > 104:
            pairs_test_file.write(str(ip) + "\t" + masked_text.replace("\n", "") + "\t" + str(label) + "\n")
            ip += 1

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her",
                     "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming",
                  "alarmed", "out of control", "help", "unhappy", "bad",
                  "upset", "awful", "broken", "damage", "damaging", "dismal",
                  "distressed", "concerning", "horrible", "horribly",
                  "questionable"]

# Converts email string into list of lines


def lst_from_email(email):
    lines_in_email = email.split('\n')
    return [word.split() for word in lines_in_email]

# Eemoves punctuation and returns striped word and it's punctuation separately


def remove_punctuation(word):
    punctuation = "{}[],./;:\'\"?!()"  # Made for easy changes
    punctuation = [i for i in punctuation]
    for i in punctuation:
        if i in word:
            word = word.strip(i)
            return word, i
    i = ""
    return word, i
# Finds word to replace and does so with restoring punctuation


def replace_word_from_lst(email, lst):
    lines_in_email_split = lst_from_email(email)
    new_email = []
    for line in lines_in_email_split:
        new_line = []  # Checked words get appended to create fixed line
        for word in line:
            word, punctuation = remove_punctuation(word)
            censorship = "".join(["-" for letter in word])
            # Takes striped word, makes it lowercase and checks if it matches
            # any item in provided list
            if word.lower() in lst:
                new_line.append(censorship + punctuation)
                continue
            new_line.append(word + punctuation)
        new_email.append(" ".join(new_line))  # Returns back the whole string
    return "\n".join(new_email)


# Looks for phrase in lowercase email string, splits the phrase to find phrase
# as separate words in line, so it can replace each word with censor line
# that hase same amout of characters and spaces as original word,
# and so no other matching word would get changed
def replace_phrase(email, lst):
    # Breakes lines into separate words
    lines_in_email_split = [line for line in lst_from_email(email)]
    lines_in_email_split_lower = lst_from_email(email.lower())
    new_email = []
    for item in lst:
        # Checks if item in list is a phrase not a word
        if len(item.split()) > 1:
            # Splits the item so each word has it's own index
            item = item.split()
            for line in lines_in_email_split_lower:
                # Save index of line
                # so it can later find the same line but uppercase
                line_index = lines_in_email_split_lower.index(line)
                i = 0
                # Adding "+1" index later and "-1"
                # so I don't get "IndexError" error
                while i < (len(item) - 1):
                    # Check if n and n+1 word of phrase are in line
                    # so only phrase gets censored;
                    # if phrase has more than 2 words
                    # then it loops till item[-2]
                    if item[i] in line\
                        and item[i + 1] in line[(line.index(item[i])) + 1]\
                            and item[i] in email.lower():
                        new_word, punctuation = remove_punctuation(
                            line[line.index(item[i])])
                        new_word_2, punctuation2 = remove_punctuation(
                            line[(line.index(item[i])) + 1])  # Strip word
                        censorship = "".join(["-" for letter in new_word])
                        # Create censored equivalent
                        censorship_2 = "".join(["-" for letter in new_word_2])
                        lines_in_email_split[line_index][(line.index(
                            item[i])) + 1] = censorship_2 + punctuation2
                        # Replace words at indexes
                        # (from lowercase) in uppercase vesrion of email list
                        lines_in_email_split[line_index][line.index(
                            item[i])] = censorship + punctuation
                    i += 1
    for line in lines_in_email_split:  # Reconstruct email string
        new_email.append(" ".join(line))

    return "\n".join(new_email)


def censor_email(email, lst):  # Censors words and phrases in email
    new_email = replace_word_from_lst(email, lst)
    new_email = replace_phrase(new_email, lst)
    return new_email

print(censor_email(email_two,proprietary_terms))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
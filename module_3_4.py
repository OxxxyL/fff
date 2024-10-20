def single_root_words(root_word, *other_words): #root = параметр корневого слова other= неограниченное кол-во аргум.
    same_words = [] #Пустой список для хранения

    for word in other_words: #Перебираем каждое слово
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    #rootlower= нижний регистр у корневого слова wordlower=приводим текущее к нижнему регистру rootword= ищет True слово
        #Same_words= если условие истинно, word добавится в список same_words
    return same_words #Теперь после завершения цикла, same вернет все слова которые соответствуют условиям

# Вызовы функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
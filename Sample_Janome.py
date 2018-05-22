# # print ('Mod Load')

# # def test( char ):
# #     from os import path
# #     p = path.join( char, 'test')
# #     print(p)

# # if __name__ == '__main__':
# #     print ('Test Yuichi')
# # #       print('てすと')

# # test('Ass')

def split_sentence( sentence ):
    from janome.tokenizer import Tokenizer

    data = []
    each_data = []

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize( sentence )

    for token in tokens:
        partOfSpeech = token.part_of_speech.split(',')[0]
        # 今回抽出するのは名詞だけとします。（もちろん他の品詞を追加、変更、除外可能です。）
        if partOfSpeech == u'名詞':
            # each_data.append(token.surface) # token.surfaceは表層形(語彙)です。詳しくはこちら...http://ailaby.com/janome/
            data.append(token.surface )
        # すべての形態素を含ませたいのであればif構文を外し、each_data.append(token.surface)のみ記載してください。
        
    # data.append(each_data)
    # each_data = []
    return data

print (split_sentence("私はサッカーが好きです。") )
"""
for token in tokens:
    partOfSpeech = token.part_of_speech.split(',')[0]
    # 今回抽出するのは名詞だけとします。（もちろん他の品詞を追加、変更、除外可能です。）
    if partOfSpeech == u'名詞':
        each_data.append(token.surface) # token.surfaceは表層形(語彙)です。詳しくはこちら...http://ailaby.com/janome/
    # すべての形態素を含ませたいのであればif構文を外し、each_data.append(token.surface)のみ記載してください。
data.append(each_data)
each_data = []
"""
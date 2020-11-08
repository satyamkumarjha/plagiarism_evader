from googletrans import Translator
import docx
import paraphrase_googletranslate

translator = Translator()
phraser = paraphrase_googletranslate.Paraphraser(random_ua=True)

doc = docx.Document('1Ch8.docx')

f = open('text.txt','a')

count = 0

for para in doc.paragraphs:
    #print(type(para.text))
    try:
        word = translator.translate(para.text,src='en',dest='ko')
        '''ward = translator.translate(word.text,src='ko',dest='ru')
        aa = translator.translate(ward.text,src=''.dest='')
        bb = translator.translate(ward.text,src=''.dest='')
        cc = translator.translate(ward.text,src=''.dest='')
        dd = translator.translate(ward.text,src=''.dest='')'''
        ee = translator.translate(word.text,src='ko',dest='en')
        #translator.detect(ee.text)
        #ee = phraser.paraphrase(ee.text)
        #det = translator.detect(ee)
        ee1 = phraser.paraphrase(ee.text)
        if ee1 is not None:
            print(ee1)
            f.write(ee1)
            f.write('\n')
        else:
            print(ee.text)
            f.write(ee.text)
            f.write('\n')
        count+=1
        print(count)
    except:
        count+=1
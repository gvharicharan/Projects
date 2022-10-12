#Install pywhatkit

import pywhatkit as pw

txt="""Sachin Ramesh Tendulkar AO BR is an Indian former international cricketer who captained the Indian national team. He is regarded as one of the greatest batsmen in the history of cricket.
He is the all time highest run-scorer in both ODI and Test Format with more than 18000 runs and 15000 runs respectively in total."""

pw.text_to_handwriting(txt,'demo1.png',[255,0,0])
print("END")
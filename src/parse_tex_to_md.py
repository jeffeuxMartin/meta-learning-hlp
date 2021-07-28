# todo: source file, Sound... (head cut)
from re import sub; from sys import argv
VERBOSE = 0
VERBOSE1 = 0
INPUTTEXT = ('\n\\begin{table}[!h]\n\\centering\n\\ca'
    'ption{Referrence of HLP tasks using different me'
    'ta-learning methods.}\n\\label{table:ref}\n  \\r'
    'esizebox{\\columnwidth}{!}{\n\\begin{tabular}{|l'
    '||l|l|l|}\n\\hline\n& (A) \\textbf{Learning to i'
    'nitialize} &  (B) \\textbf{Learning to compare}&'
    '  (C) \\textbf{Other}  \\\\ \\hline\\hline\n\n S'
    'ound Event Detection  &   \\cite{Shi:ICASSP20} '
    '\n & \\tabincell{l}{\\cite{Shimada:arXiv19}\\\\'
    '\\cite{Chou:ICASSP19}\\\\\\cite{Wang:ICASSP20} '
    '\\\\\\cite{Shimada:ICASSP20} \\\\ \\cite{Shi:ICA'
    'SSP20} }\n &    \\tabincell{l}{ Network architec'
    'ture search: \\\\\\cite{Li:INTERSPEECH20} }   \\'
    '\\ \\hline\n\nKeyword Spotting &  \\cite{Chen:ar'
    'Xiv18}       &  \\cite{Huh:arXiv20}  & \n \\tabi'
    'ncell{l}{ Net2Net: \\\\ \\cite{Veniat:ICASSP19} '
    '\\\\ \n Network architecture search: \\\\\\cite{'
    'Mazzawi:INTERSPEECH19} \\\\\n  Network architect'
    'ure search: \\\\\\cite{Mo:INTERSPEECH20}  } \\\\'
    '  \\hline\n\n %   Speaker Recognition &    & \\c'
    'ite{Anand:arXiv19}    &  \\\\ \\hline\n \n  Text'
    ' Classification & \\tabincell{l}{\\cite{Dou:EMNL'
    'P19}\\\\\\cite{Bansal:arXiv19}} & \\tabincell{l}'
    '{\\cite{Yu:ACL18}\\\\\\cite{Tan:EMNLP19}\\\\\\ci'
    'te{Geng:EMNLP19}\\\\\\cite{Sun:EMNLP19}} & \n \\'
    'tabincell{l}{Learning the learning algorithm:\\'
    '\\ \\cite{Wu:EMNLP19}} \\\\ \\hline\n \n Voice C'
    'loning& & & \\tabincell{l}{Learning the learning'
    ' algorithm:\\\\\\cite{Chen:ICLR19} \\\\  \\cite{'
    'Serra:NeurIPS19}} \\\\\\hline\n \n Sequence Labe'
    'lng & \\cite{Wu:AAAI20} & \\cite{Hou:ACL20} & \\'
    '\\ \\hline\n \n Machine Translation  & \\tabince'
    'll{l}{\\cite{Gu:EMNLP18}\\\\\\cite{Indurthi:arXi'
    'v19}}&  &     \\\\ \\hline\n Speech Recognition&'
    ' \\tabincell{l}{\\cite{Hsu:ICASSP20}\\\\ \\cite{'
    'Klejch:ASRU19} \\\\ \\cite{Winata:ACL2020} \\\\ '
    '\\cite{Winata:INTERSPEECH2020} } &      & \\tabi'
    'ncell{l}{Learning to optimize:\\\\\\cite{Klejch:'
    'INTERSPEECH18} \\\\ Network architecture search:'
    ' \\\\ \\cite{Chen:INTERSPEECH20}\\\\ \\cite{Baru'
    'wa:IJSER19} } \\\\ \\hline\n \n Knowledge Graph '
    ' & \\tabincell{l}{\\cite{Obamuyide:ACL19}\\\\\\c'
    'ite{Bose:arXiv19}\\\\\\cite{Lv:EMNLP19}\\\\\\cit'
    'e{Wang:EMNLP19}}& \\tabincell{l}{\\cite{Ye:ACL19'
    '}\\\\\\cite{Chen:EMNLP19}\\\\\\cite{Xiong:EMNLP1'
    '8}\\\\\\cite{Gao:AAAI19}}& \\\\ \\hline\n \n Dia'
    'logue / Chatbot  & \\tabincell{l}{\\cite{Qian:AC'
    'L19}\\\\\\cite{Madotto:ACL19}\\\\\\cite{Mi:IJCAI'
    '19}}& & \\tabincell{l}{Learning to optimize: \\'
    '\\ \\cite{Chien:INTERSPEECH19} } \\\\ \\hline\nP'
    'arsing & \\tabincell{l}{\\cite{Guo:ACL19}\\\\\\c'
    'ite{Huang:NAACL18}} &    & \\\\ \\hline\n Word E'
    'mbedding  &  \\cite{Hu:ACL19}    &\\cite{Sun:EMN'
    'LP18}      &    \\\\ \\hline\n Multi-model & &\\'
    'cite{Eloff:ICASSP19}& \\tabincell{l}{Learning th'
    'e learning algorithm: \\\\\\cite{Suris:arXiv19} '
    '}\\\\ \\hline\n\n \\end{tabular}\n}\n\n\\end{tab'
    'le}\n\n')

def processor(INPUTTEXT):
    inputtext = INPUTTEXT[:]
    
    # filter comments
    inputtext = '\n'.join([l.split('%')[0] 
                    for l in inputtext.split('\n')])

    inputtext = inputtext.strip()
    inputtext = inputtext.replace("\\\\", " \\\\ ")
    inputtext = inputtext.replace("&", " & ")
    inputtext = inputtext.replace("\n", " ")
    out_inputtext = inputtext.replace("  ", " ")
    while out_inputtext != inputtext:
        inputtext = out_inputtext
        out_inputtext = inputtext.replace("  ", " ")
    inputtext = out_inputtext
    del out_inputtext

    inputtext = inputtext.replace('\\hline', '|\n|')
    # inputtext = inputtext.replace('\\\\', '<br />')
    inputtext = inputtext.replace('\\\\', '<br />')
    inputtext = inputtext.replace('&', '|')

    # print(inputtext)

    """
    inputtext = inputtext.replace(
        '\\begin{table}[!h] \\centering \\caption{Ref'
        'errence of HLP tasks using different meta-le'
        'arning methods.} \\label{table:ref} \\resize'
        'box{\\columnwidth}{!}{ \\begin{tabular}{|l||'
        'l|l|l|} | \n     | (A) \\textbf{Learning to i'
        'nitialize} | (B) \\textbf{Learning to compare'
        '} | (C) \\textbf{Other} <br /> | \n    | ',
        '|-|-|-|-|\n|-|-|-|-|')
    """
    fbeg = inputtext.index(
        "\\begin{tabular}{|l||l|l|l|}") + len(
        "\\begin{tabular}{|l||l|l|l|}") + 2
    
    inputtext = inputtext[fbeg:]
    # inputtext = "|-|-|-|-|\n|" + inputtext
    # inputtext = (" | | "
    #     "(A) \\textbf{Learning to initialize} | "
    #     "(B) \\textbf{Learning to compare} | "
    #     "(C) \\textbf{Other} | \n") + inputtext
    fend = inputtext.index("\\end{tabular}")
    inputtext = inputtext[:fend]

    inputtext = inputtext.replace("\n| |\n", "\n|-|-|-|-|\n", 1)

    if VERBOSE1:
        with open(argv[2], 'w') as f:
            f.write(inputtext)
        input('===raw')
    inputtext = inputtext.replace(
        r""" \end{tabular} } \end{table}""", '')
    if VERBOSE1:
        with open(argv[2], 'w') as f:
            f.write(inputtext)
        input('===remove end')
    inputtext = inputtext.replace("| <br /> |", '| |')
    if VERBOSE1:
        with open(argv[2], 'w') as f:
            f.write(inputtext)
        input('===remove empty cells')
    inputtext = sub(
        r"\\cite{([\w:-]*)}", r'[\g<1>]', inputtext)
    if VERBOSE:
        with open(argv[2], 'w') as f:
            f.write(inputtext)
        input('===remove \\cite to []')
    out_inputtext = sub(
        r"\\tabincell{l}{([\[\w\s\\:-\]\/]*)}", 
        r'\g<1>', inputtext)
    while out_inputtext != inputtext:
        inputtext = out_inputtext
        out_inputtext = sub(
            r"\\tabincell{l}{([\[\w\s\\:-\]\/]*)}", 
            r'\g<1>', inputtext)
    inputtext = out_inputtext
    del out_inputtext

    inputtext = sub(
        r"\\tabincell\{l\}\{([\[\w\-\s\<\/\>\]\:]*)\}", 
        r'\g<1>', inputtext)
    if VERBOSE:
        with open(argv[2], 'w') as f:
            f.write(inputtext)
        input('===remove \\tabincell')

    inputtext = inputtext.replace("<br /> |", "|")
    if VERBOSE:
        with open(argv[2], 'w') as f:
            f.write(inputtext)
        input('===remove empty end')
    if inputtext[-2:] == "| ":
        inputtext = inputtext[:-2]

    I = inputtext.split('\n')
    if I[2].replace(' ', '') == '||':
        inputtext = [I[0], I[1], '|-|-|-|-|'] + I[3:]
        inputtext = '\n'.join(inputtext)

    inputtext = sub(
        r"\\textbf{([\[\w\s\\:-\]\/]*)}", 
        r'**\g<1>**', inputtext)
    inputtext = inputtext.replace("(C)", "\(C)")
    inputtext = inputtext.replace("(c)", "\(c)")
    return inputtext

if len(argv) > (1):
    with open(argv[1], 'r') as f:
        INPUTTEXT = f.read()
inputtext = processor(INPUTTEXT)
if len(argv) > (2):
    with open(argv[2], 'w') as f:
        f.write(inputtext)
else:
    with open('check.md', 'w') as f:
        f.write(inputtext)
if 0:
    X = '|| Text Classification | \\tabincell{l}{[Dou:EMNLP19] <br /> [Bansal:arXiv19] <br /> [holla-etal-2020-learning] <br /> [MetaKD-arXiv21] <br /> [van-der-heijden-etal-2021-multilingual] <br /> [bansal-etal-2020-self] <br /> [murty-etal-2021-dreca]} | \\tabincell{l}{[Yu:ACL18] <br /> [Tan:EMNLP19] <br /> [Geng:EMNLP19] <br /> [Sun:EMNLP19] <br /> [geng2020dynamic]} | \\tabincell{l}{Learning the learning algorithm: <br /> [Wu:EMNLP19] <br /> Network architecture search: <br /> [pasunuru2020fenas] <br /> [pasunuru2019continual] <br /> \\tabincell{l}{Learning to optimize:} <br /> [learningToOptimize:metaNLP21] <br /> Learning to select data: <br /> [label-correction-aaai21]} <br /> |'
    Y = '|| Text Classification | [Dou:EMNLP19] <br /> [Bansal:arXiv19] <br /> [holla-etal-2020-learning] <br /> [MetaKD-arXiv21] <br /> [van-der-heijden-etal-2021-multilingual] <br /> [bansal-etal-2020-self] <br /> [murty-etal-2021-dreca] | [Yu:ACL18] <br /> [Tan:EMNLP19] <br /> [Geng:EMNLP19] <br /> [Sun:EMNLP19] <br /> [geng2020dynamic] | Learning the learning algorithm: <br /> [Wu:EMNLP19] <br /> Network architecture search: <br /> [pasunuru2020fenas] <br /> [pasunuru2019continual] <br /> Learning to optimize: <br /> [learningToOptimize:metaNLP21] <br /> Learning to select data: <br /> [label-correction-aaai21] <br /> |'

    def R(G):
        from re import sub
        return sub(G, r'\g<1>', X)

    def K(G):
        Z = R(G)
        print(X); print()
        print(Z); print()
        print(Y); print()

    K(r"\\tabincell\{l\}\{([\[\w\-\s\<\/\>\]\:]*)\}")
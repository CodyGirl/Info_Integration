import Levenshtein as lev
import csv
import pandas as pd
import math

databaseTask2 = 'info_integration_task2' 
username = 'root' 
password = 'mysql'

datasource1 = list(pd.read_csv("universities_ranking.csv",nrows=1).columns)
print(datasource1)

datasource2 = list(pd.read_csv("2020-QS-World-University-Rankings.csv",nrows=1).columns)
print(datasource2)

datasource3 = list(pd.read_excel("World University Rankings 2019-20.xlsx",nrows=1).columns)
print(datasource3)

final_mapping = []
for i in datasource3:
    max_score_Ratio = []
    for j in datasource1:
        ratio = lev.ratio(i.lower(),j.lower())
        temp = {'i' : i,'j': j, 'ratio': ratio}
        max_score_Ratio.append(temp)
    max = max_score_Ratio[0]
    for val in max_score_Ratio:
        if(val['ratio'] > max['ratio']):
            max = val
    final_mapping.append(max)

print(final_mapping)



# datasource QS and World Ranking
# [{'i': 'Rank in 2020', 'j': 'World Rank', 'ratio': 0.36363636363636365}, {'i': 'Rank in 2019', 'j': 'World Rank', 'ratio': 0.36363636363636365}, {'i': 'Institution Name', 'j': 'Institution', 'ratio': 0.8148148148148148}, {'i': 'Country', 'j': 'Score', 'ratio': 0.5}, {'i': 'Classification', 'j': 'Location', 'ratio': 0.6363636363636364}, {'i': 'Academic Reputation', 'j': 'Quality\xa0of Education', 'ratio': 0.5128205128205129}, {'i': 'Employer Reputation', 'j': 'Location', 'ratio': 0.5185185185185186}, {'i': 'Faculty Student', 'j': 'Alumni Employment', 'ratio': 0.4375}, {'i': 'Citations per Faculty', 'j': 'Quality\xa0of Faculty', 'ratio': 0.5641025641025641}, {'i': 'International Faculty', 'j': 'National Rank', 'ratio': 0.5882352941176471}, {'i': 'International Students', 'j': 'National Rank', 'ratio': 0.5714285714285715}, {'i': 'Overall Score', 'j': 'Score', 'ratio': 0.5555555555555556}, {'i': 'SIZE', 'j': 'Score', 'ratio': 0.4444444444444444}, {'i': 'FOCUS', 'j': 'Location', 'ratio': 0.3076923076923077}, {'i': 'RESEARCH INTENSITY', 'j': 'Research Performance', 'ratio': 0.5789473684210527}, {'i': 'AGE', 'j': 'Score', 'ratio': 0.25}, {'i': 'STATUS', 'j': 'Institution', 'ratio': 0.4705882352941177}, {'i': 'SCORE', 'j': 'Score', 'ratio': 1.0}, {'i': 'RANK', 'j': 'World Rank', 'ratio': 0.5714285714285715}, {'i': 'SCORE.1', 'j': 'Score', 'ratio': 0.8333333333333333}, {'i': 'RANK.1', 'j': 'World Rank', 'ratio': 0.5}, {'i': 'SCORE.2', 'j': 'Score', 'ratio': 0.8333333333333333}, {'i': 'RANK.2', 'j': 'World Rank', 'ratio': 0.5}, {'i': 'SCORE.3', 'j': 'Score', 'ratio': 0.8333333333333333}, {'i': 'RANK.3', 'j': 'World Rank', 'ratio': 0.5}, {'i': 'SCORE.4', 'j': 'Score', 'ratio': 0.8333333333333333}, {'i': 'RANK.4', 'j': 'World Rank', 'ratio': 0.5}, {'i': 'SCORE.5', 'j': 'Score', 'ratio': 0.8333333333333333}, {'i': 'RANK.5', 'j': 'World Rank', 'ratio': 0.5}, {'i': 'Unnamed: 29', 'j': 'National Rank', 'ratio': 0.33333333333333326}]
# datasource QS and university_ranking
# [{'i': 'Rank in 2020', 'j': 'ranking', 'ratio': 0.631578947368421}, {'i': 'Rank in 2019', 'j': 'ranking', 'ratio': 0.631578947368421}, {'i': 'Institution Name', 'j': 'title', 'ratio': 0.38095238095238093}, {'i': 'Country', 'j': 'location', 'ratio': 0.4}, {'i': 'Classification', 'j': 'location', 'ratio': 0.6363636363636364}, {'i': 'Academic Reputation', 'j': 'gender ratio', 'ratio': 0.5161290322580645}, {'i': 'Employer Reputation', 'j': 'gender ratio', 'ratio': 0.5806451612903225}, {'i': 'Faculty Student', 'j': 'perc intl students', 'ratio': 0.6060606060606061}, {'i': 'Citations per Faculty', 'j': 'location', 'ratio': 0.41379310344827586}, {'i': 'International Faculty', 'j': 'gender ratio', 'ratio': 0.4242424242424242}, {'i': 'International Students', 'j': 'perc intl students', 'ratio': 0.7}, {'i': 'Overall Score', 'j': 'perc intl students', 'ratio': 0.3870967741935484}, {'i': 'SIZE', 'j': 'title', 'ratio': 0.4444444444444444}, {'i': 'FOCUS', 'j': 'location', 'ratio': 0.3076923076923077}, {'i': 'RESEARCH INTENSITY', 'j': 'perc intl students', 'ratio': 0.5555555555555556}, {'i': 'AGE', 'j': 'ranking', 'ratio': 0.4}, {'i': 'STATUS', 'j': 'number students', 'ratio': 0.38095238095238093}, {'i': 'SCORE', 'j': 'location', 'ratio': 0.3076923076923077}, {'i': 'RANK', 'j': 'ranking', 'ratio': 0.7272727272727272}, {'i': 'SCORE.1', 'j': 'location', 'ratio': 0.2666666666666667}, {'i': 'RANK.1', 'j': 'ranking', 'ratio': 0.6153846153846154}, {'i': 'SCORE.2', 'j': 'location', 'ratio': 0.2666666666666667}, {'i': 'RANK.2', 'j': 'ranking', 'ratio': 0.6153846153846154}, {'i': 'SCORE.3', 'j': 'location', 'ratio': 0.2666666666666667}, {'i': 'RANK.3', 'j': 'ranking', 'ratio': 0.6153846153846154}, {'i': 'SCORE.4', 'j': 'location', 'ratio': 0.2666666666666667}, {'i': 'RANK.4', 'j': 'ranking', 'ratio': 0.6153846153846154}, {'i': 'SCORE.5', 'j': 'location', 'ratio': 0.2666666666666667}, {'i': 'RANK.5', 'j': 'ranking', 'ratio': 0.6153846153846154}, {'i': 'Unnamed: 29', 'j': 'number students', 'ratio': 0.3076923076923077}]
# datasource university_ranking and World Ranking
# [{'i': 'World Rank', 'j': 'ranking', 'ratio': 0.4705882352941177}, {'i': 'Institution', 'j': 'location', 'ratio': 0.4210526315789474}, {'i': 'Location', 'j': 'location', 'ratio': 1.0}, {'i': 'National Rank', 'j': 'location', 'ratio': 0.4761904761904762}, {'i': 'Quality\xa0of Education', 'j': 'location', 'ratio': 0.5714285714285715}, {'i': 'Alumni Employment', 'j': 'number students', 'ratio': 0.375}, {'i': 'Quality\xa0of Faculty', 'j': 'students staff ratio', 'ratio': 0.31578947368421056}, {'i': 'Research Performance', 'j': 'gender ratio', 'ratio': 0.375}, {'i': 'Score', 'j': 'location', 'ratio': 0.3076923076923077}]


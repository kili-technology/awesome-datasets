import numpy as np
import pandas as pd
import re



def to_shortcut(text):
    return re.sub("[^0-9a-zA-Z]+", "-", text.lower())


class Document:

    _md = ''

    def __init__(self):
        self._df = pd.read_csv('./dataset.csv', sep=';')

    
    def make(self):
        self._introduction()
        for industry in np.sort(self._df.Industry.unique()):
            self._md += f"""

<h1 id="{to_shortcut(industry)}">{industry}</h1>
"""
            self._industry_table_of_content(industry)
            df_industry = self._df.loc[self._df.Industry == industry, :]
            for department in np.sort(df_industry.Department.unique()):
                department_shortcut = to_shortcut(industry) + "-" + to_shortcut(department)
                self._md += f"""
<h2 id="{department_shortcut}">{department}</h2>
"""
                df_department = df_industry.loc[self._df.Department == department, :]
                for use_case in np.sort(df_department.UseCase.unique()):
                    use_case_shortcut = department_shortcut +  "-" + to_shortcut(use_case)
                    self._md += f"""
<h3 id="{use_case_shortcut}">{use_case}</h3>

"""
                    df_use_case = df_department.loc[self._df.UseCase == use_case, :]
                    for ml_task in np.sort(df_use_case.MLTask.unique()):
                        df_ml_task = df_use_case.loc[self._df.MLTask == ml_task, :]
                        self._md += f"{ml_task}:\n\n"
                        for _, row in df_ml_task.iterrows():
                            self._md += f"- [{row.Name}]({row.Url}) {row.Description}\n"
                        self._more_datasets(industry, department, use_case, ml_task)

        return self._md

    
    def _introduction(self):
        h1 = []
        for industry in np.sort(self._df.Industry.unique()):
            h1.append(f"- [{industry}](#{to_shortcut(industry)})")    
        self._md = """
<div align="center">
  <h1>Awesome Datasets</h1>
</div>

We're collecting (an admittedly opinionated) public data sources in high quality. Most of the data sets listed below are free, however, some are not. They are classified by industry and use case.

*We're only at the beginning, and you can help by contributing to this GitHub!*

<!-- omit in toc -->
## How Can I Help?

If you're interested in this area and would like to hear more, join our [Slack community (coming soon)](#)! We'd also appreciate if you could fill out this short [form (coming soon)](#) to help us better understand what your interests might be.

<!-- omit in toc -->
### Feedback

If you have ideas on how we can make this repository better, feel free to submit an issue with suggestions.

<!-- omit in toc -->
### Contributing

We want this resource to grow with contributions from readers and data enthusiasts. If you'd like to make contributions to this Github repository, please read our contributing guidelines.

<!-- omit in toc -->
# Table of Content

""" \
    + '\n'.join(h1)


    def _industry_table_of_content(self, industry):
        df_industry = self._df.loc[self._df.Industry == industry, :]
        for department in np.sort(df_industry.Department.unique()):
            department_shortcut = to_shortcut(industry) + "-" + to_shortcut(department)
            self._md += f"""
- [{department}](#{department_shortcut})"""
            df_department = df_industry.loc[self._df.Department == department, :]
            for use_case in np.sort(df_department.UseCase.unique()):
                use_case_shortcut = department_shortcut +  "-" + to_shortcut(use_case)
                self._md += f"""
  - [{use_case}](#{use_case_shortcut})"""

    def _more_datasets(self, industry, department, use_case, ml_task):
        index = (self._df.MLTask == ml_task) & (
            (self._df.Industry != industry) \
                | (self._df.Department != department) \
                | (self._df.UseCase != use_case))
        more_df = self._df.loc[index, :].sort_values(by=['Industry', 'Department', 'UseCase'])
        if len(more_df) == 0:
            return
        self._md += f"""
<details>
  <summary style="font-style: italic;">Click to get more datasets from other industries and use cases</summary>

"""
        for _, row in more_df.iterrows():
            shortcut = to_shortcut(industry) + "-" + to_shortcut(department) +  "-" + to_shortcut(use_case)
            self._md += f"- [{row.Industry} > {row.Department} > {row.UseCase}]({shortcut})\n"
        self._md += "</details>\n"




if __name__ == '__main__':
    document = Document()
    with open('./README.md', 'w') as handler:
        handler.write(document.make())
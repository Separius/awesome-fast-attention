import re
import json
import urllib.parse
import urllib.request
from time import gmtime, strftime
from operator import attrgetter, itemgetter

import arxiv
from tqdm import tqdm
from natsort import natsorted

github_prefix = 'https://github.com/'
github_prefix_len = len(github_prefix)
arxiv_papers = set()


def get_and_sort_meta_info(json_file):
    with open(json_file) as f:
        meta_info = json.load(f)
    meta_info = natsorted(meta_info, key=itemgetter('arxiv_id'))
    with open(json_file, 'w') as f:
        f.write(json.dumps(meta_info, indent=2))
    return meta_info


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def fancy_code(code_link):
    if code_link == 'IN_PAPER':
        return code_link
    if code_link.startswith(github_prefix):
        tmp = code_link[github_prefix_len:]
        if tmp.endswith('/'):
            tmp = tmp[:-1]
        if len(re.findall('/', tmp)) > 2:
            tmp = tmp[:find_nth(tmp, '/', 2)]
        code_name = tmp.split('/')[1]
        github_stars = ' ![](https://img.shields.io/github/stars/{}.svg?style=social )'.format(tmp)
    else:
        code_name = 'code'
        github_stars = ''
    return f'[{code_name}]({code_link} ){github_stars}'


def query_semantic_scholar(query):
    if query == '':
        return 'N/A', '-'
    try:
        global arxiv_papers
        if query in arxiv_papers:
            raise ValueError('Duplicate Paper {}'.format(query))
        arxiv_papers.add(query)
        res = json.loads(urllib.request.urlopen("https://api.semanticscholar.org/v1/paper/" + query).read())
        count = len(res['citations'])
        return (str(count) if count < 999 else '999+'), str(res['year']) + '/??'
    except:
        return 'N/A', '-'


def query_arxiv_api(arxiv_id):
    res = arxiv.query(id_list=[arxiv_id])[0]
    return ' '.join(res['title'].strip().replace('\n', ' ').split()), res['arxiv_url'].replace('http:', 'https:'), res['summary']


def fetch_common_parts(paper):
    arxiv_id = paper['arxiv_id']
    arxiv_date = arxiv_id.split('.')[0]
    date_part = '20' + arxiv_date[:2] + '/' + arxiv_date[2:]
    citation_part, _ = query_semantic_scholar('arXiv:{}'.format(arxiv_id))
    paper_title, paper_link, paper_abstract = query_arxiv_api(arxiv_id)
    paper_part = f'[{paper_title}]({paper_link} )'
    return citation_part, date_part, paper_part, paper_abstract


def make_expandable(comment):
    return f'<details><summary>EXPAND</summary><p>{comment}</p></details>'


def render_complexity(complexity_latex):
    complexity = complexity_latex.replace('*', '\\cdot').replace('+', '%2b')
    return '![formula](https://render.githubusercontent.com/render/math?math=\\mathcal{O}(' + f'{complexity}))'


def generate_fast_attention_table():
    header = [
        '|Paper (citations)|Implementation|Computational Complexity|AutoRegressive|Main Idea|',
        '|:---:|:---:|:---:|:---:|:---:|']
    generated_lines = []
    meta_info = get_and_sort_meta_info('FastAttention.json')
    for item in tqdm(meta_info):
        citation, date, paper, abstract = fetch_common_parts(item)
        if 'code' in item:
            code = fancy_code(item['code'])
        else:
            code = '-'
        generated_lines.append(
            AttrDict(date=date, name=item['name'], paper=paper, auto=':heavy_check_mark:' if item['causal'] else ':x:',
                     idea=make_expandable(item['comment']), complexity=render_complexity(item['complexity']),
                     citation=citation, code=code))
    generated_lines = sorted(generated_lines, key=attrgetter('date', 'citation'))
    generated_lines = ['|{paper} ({citation})|{code}|{complexity}|{auto}|{idea}|'.format(**x)
                       for x in generated_lines]
    return '\n'.join(header + generated_lines)


if __name__ == '__main__':
    with open('README_BASE.md', 'r') as f:
        readme = f.read()
    readme = readme.replace('{{{generation-date}}}', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
    readme = readme.replace('{{{fast-attention-table}}}', generate_fast_attention_table())
    with open('README.md', 'w') as f:
        f.write(readme)

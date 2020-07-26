card = """
<div class="card text-center shadow-lg mb-5 bg-white rounded">
  <div class="card-header {}">
  {}
  </div>
  <div class="card-body">
	<h5 class="card-title">{}</h5>
	<p class="card-text">{}</p>
  </div>
</div>"""

# Layout Templates
jumbo = """<div class=" jumbotron shadow-lg {bg}">{inner_jumbo}</div>"""
inner = """ <h1 style="text-align:center;" class="display-4 mx-5">{title}</h1>
  <h3 class="lead">{subtitle}</h3>
  <hr class="my-4">
  {description}
  """
title_temp = """
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<h6>Author:{}</h6>
	<br/>
	<br/>
	<p style="text-align:justify">{}</p>
	</div>
	"""
article_temp = """
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<h6>Author:{}</h6>
	<h6>Post Date: {}</h6>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>
	<p style="text-align:justify">{}</p>
	</div>
	"""
head_message_temp = """
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
	<h6>Author:{}</h6>
	<h6>Post Date: {}</h6>
	</div>
	"""
full_message_temp = """
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<p style="text-align:justify;color:black;padding:10px">{}</p>
	</div>
	"""

list_group_temp = """<div class="mx-5 list-group rounded-pill shadow-lg">{}</div>"""
hori_list_group_temp = """<div class="my-2 list-group list-group-horizontal rounded-pill shadow">{}</div>"""
list_group_item_temp = """<button type="button" class="list-group-item list-group-item-action list-group-item-{bg}">{text}</button>"""
feat_group_item_temp = """<button type="button" class=" d-flex justify-content-between align-items-center list-group-item list-group-item-action list-group-item-{bg}">{text}<span class="mx-1 badge badge-{percent_status} badge-pill">{percent}%</span></button>"""

two_col_temp = """
 <div class="col">
      <h3>{}</h3>
    <div class="row">
      {}
    </div>
      <h3>{}</h3>
    <div class="row">
      {}
    </div>
  </div>
"""


def divide_chunks(l, n):

    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def list_group_render(page_data):
    return list_group_temp.format([
        list_group_item_temp.format_map({
            'bg': page_data['bg'],
            'text': i
        }) for i in page_data['description'].split('. ')
    ]).replace('\'', '').replace('[', '').replace(']', '').replace(',', '')
def list_render(data_list, bg, missing_df):
	n = 4
	final = [data_list[i * n:(i + 1) * n] for i in range((len(data_list) + n - 1) // n)]
	return ' '.join([hori_list_group_temp.format([
        feat_group_item_temp.format_map({
            'bg': bg,
            'text': i.title(),
			'percent': missing_df[i],
			'percent_status': percent_gate(missing_df[i])
        }) for i in data
    ]).replace('\'', '').replace('[', '').replace(']', '').replace(',', '')
	for data in final])
# TODO create a class for bundling templates with themes

# class ThemeContext(object):


def percent_gate(percent):
	if percent > 90:
		return 'success'
	elif percent > 75:
		return 'warning'
	else:
		return 'danger'

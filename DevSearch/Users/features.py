from django.core.paginator import EmptyPage, Paginator

def pagination(request, all_items):
	# Get projects depending on the page.
	items_per_page = 10
	page = 1

	if request.GET.get('page'):
		page = request.GET.get('page')

	p = Paginator(all_items, items_per_page)

	try:
		items = p.page(page)
	except EmptyPage:
		# If page is out of range, deliver last page of results.
		items = p.page(p.num_pages)

	# Left range of the current page.
	leftRange = int(page) - 4

	# If leftRange is less than 1 then set it to 1.
	if leftRange < 1:
		leftRange = 1
	
	# Right range of the current page.
	rightRange = int(page) + 5

	# If rightRange is greater than the total number of pages then set it to the total number of pages.
	if rightRange > p.num_pages:
		rightRange = p.num_pages + 1

	# Create a range of the current page.
	custom_range = range(leftRange, rightRange)

	return items, custom_range, p, page
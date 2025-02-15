# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
	assert len(args) > 0
	for item in items:				
		if len(args) == 1:
			yield item.get(args[0]) if item.get(args[0]) is not None else None
		else:
			yield {field_name: item.get(field_name) for field_name in args if item.get(field_name) is not None} if {field_name: item.get(field_name) for field_name in args if item.get(field_name) is not None} else None

def main():
	goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 	]
	print(*field(goods,'title', 'color'))
	return


if __name__ == "__main__":
    main()

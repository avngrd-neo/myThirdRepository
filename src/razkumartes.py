import time
import random


def main(bulling_words: list) -> None:
	while not time.sleep(0.02):
		print(random.choice(bulling_words))
	


if __name__ == '__main__':
	input_str = input("Введите через запятую набор оскарбительных слов\n")
	bulling_words = list(input_str.split(','))
	try:
		main(bulling_words=bulling_words)

	except KeyboardInterrupt:
		pass


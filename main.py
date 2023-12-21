from recttangel import Rectangle
import logging
import argparse

logging.basicConfig(filename='Log/log_dz.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} функция "{funcName}()"'
                           ' строка {lineno} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Принимает действия: периметор(perimeter), площадь(area), значения(str)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Принимаем ширату, высоту, действие")
    parser.add_argument('-wid', type=int, default=1)
    parser.add_argument('-hei', type=int, default=1)
    parser.add_argument('-fun', type=str, default='perimeter')



    args = parser.parse_args()

    rect = Rectangle(args.wid, args.hei)
    match args.fun:
        case 'perimeter':
            print(rect.perimeter())
            logger.info(
                f'Переданые данные: {args.wid} ширина, {args.hei} высота, {args.fun} функция'
            )
        case 'area':
            print(rect.area())
            logger.info(
                f'Переданые данные: {args.wid} ширина, {args.hei} высота, {args.fun} функция'
            )
        case 'str':
            print(rect.__str__())
            logger.info(
                f'Переданые данные: {args.wid} ширина, {args.hei} высота, {args.fun} функция'
            )
        case _:
            print('Неверная функция')
            logger.info(
                f'Переданые данные: {args.wid} ширина, {args.hei} высота, {args.fun} функция'
                f' функция:"{args.fun}". Функция не опознана'
            )


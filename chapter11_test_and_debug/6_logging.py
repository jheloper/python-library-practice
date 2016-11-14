import logging

logformat = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename='./tmp/test.log', level=logging.DEBUG, format=logformat)

logging.debug('debug message')
logging.warning('warning message')

favorite_thing = 'bouldering'

logging.error('I love %s!', favorite_thing)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')

logger = logging.getLogger('hoge.fuga.piyo')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('./tmp/test2.log')
handler.setLevel(logging.INFO)

filter = logging.Filter('hoge.fuga')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
handler.addFilter(filter)
logger.addHandler(handler)
logger.addFilter(filter)

logger.debug('debug message')
logger.info('info message')

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from ask import alexa
import car_accidents


def lambda_handler(request_obj, context=None):
    return alexa.route_request(request_obj)


@alexa.default
def default_handler(request):
    logger.info('default_handler')
    return alexa.respond("Sorry, I don't understand.", end_session=True)


@alexa.request("LaunchRequest")
def launch_request_handler(request):
    logger.info('launch_request_handler')
    return alexa.respond('You can ask me about car accidents.', end_session=True)


@alexa.request("SessionEndedRequest")
def session_ended_request_handler(request):
    logger.info('session_ended_request_handler')
    return alexa.respond('Goodbye.', end_session=True)


@alexa.intent('AMAZON.CancelIntent')
def cancel_intent_handler(request):
    logger.info('cancel_intent_handler')
    return alexa.respond('Okay.', end_session=True)


@alexa.intent('AMAZON.HelpIntent')
def help_intent_handler(request):
    logger.info('help_intent_handler')
    return alexa.respond('You can ask me about car accidents.', end_session=True)


@alexa.intent('AMAZON.StopIntent')
def stop_intent_handler(request):
    logger.info('stop_intent_handler')
    return alexa.respond('Okay.', end_session=True)


@alexa.intent('CarAccidents')
def car_accidents_intent_handler(request):
    logger.info('car_accidents_intent_handler')
    logger.info(request.get_slot_map())

    city = request.get_slot_value('city')
    year = request.get_slot_value('year')

    if not city:
        return alexa.respond('Sorry, which city?')

    num_card_acc = car_accidents.get_num_accidents(year=int(year), city=city)
    logger.info('%s accidents in %s in %s', num_card_acc, city, year)

    return alexa.respond(
        '''
          <speak>
          There were
          <say-as interpret-as="cardinal">%s</say-as>
          car accidents in %s in
          <say-as interpret-as="date" format="y">%s</say-as>,
          </speak>
        ''' % (num_card_acc, city, year),
        end_session=True, is_ssml=True)


@alexa.intent('PopulationSweden')
def population_intent_handler(request):
    logger.info('population_sweden_intent_handler')
    logger.info(request.get_slot_map())
    year = request.get_slot_value('year')
    return alexa.respond(
        '''
          <speak>
          The population of %s was
          <say-as interpret-as="cardinal">%s</say-as>
          in
          <say-as interpret-as="date" format="y">%s</say-as>,
          </speak>
        ''' % (country, 5000, year),
        end_session=True, is_ssml=True)

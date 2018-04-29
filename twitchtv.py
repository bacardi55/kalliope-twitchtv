from twitch import TwitchClient

from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException

import logging
logging.basicConfig()
logger = logging.getLogger("kalliope")


class Twitchtv (NeuronModule):
    def __init__(self, **kwargs):
        super(Twitchtv, self).__init__(**kwargs)

        # Get parameters form the neuron
        self.configuration = {
            "client_id": kwargs.get('client_id', None),
            "limit": kwargs.get('limit', 55),
            "user": kwargs.get('user', None)
        }

        # Check parameters:
        if self._is_parameters_ok():
            client = TwitchClient(client_id=self.configuration['client_id'])

            ids = []
            for u in client.users.translate_usernames_to_ids([self.configuration['user']]):
                follows = client.users.get_follows(u.id, self.configuration['limit'])
                for i, f in enumerate(follows):
                    ids.append(f['channel']['id'])

            logger.debug('TwitchTV retrieved Ids: %s' % ','.join(ids))
            streams = client.streams.get_live_streams(','.join(ids))
            response = []
            for s in streams:
                response.append({
                    'name': s['channel']['display_name'],
                    'status': s['channel']['status'],
                    'url': s['channel']['url']
                })

            logger.debug('Twitch TV API response: %s' % response)

            message = {
                'number': len(response),
                'streamers': response
            }
            self.say(message)

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: InvalidParameterException
        """

        if self.configuration['client_id'] is None:
            raise InvalidParameterException("Twitch tv requires a client ID")

        if self.configuration['user'] is None:
            raise InvalidParameterException("User required for Twitch TV")

        return True

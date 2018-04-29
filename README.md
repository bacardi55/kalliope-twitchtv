# kalliope-wwtime

A simple [Twitch TV](https://twitch.tv) neuron to ask who are the players that you follow that are online right now.

## Synopsis

This neuron will retrieve a list of streamers that you follow and are online now.

## Installation

```
kalliope install --git-url https://github.com/bacardi55/kalliope-twitchtv.git
```


## Options

| parameter | required | default | choices | comment                                       |
|-----------|----------|---------|---------|-----------------------------------------------|
| client_id | yes      |         | string  | Your client ID from the twitch developer area |
| limit     | no       | 55      | Integer | The maximum number of results                 |
| user      | yes      |         | string  | Your username                                 |



## Return Values

| Name       | Description                               | Type       | sample                                                                  |
| ---------- | ----------------------------------------- | ---------- | ----------------------------------------------------------------------- |
| number     | The number of players online              | Integer    | The number of streamers                                                 |
| streamers  | A list of streamers name and description  | Lift       | List of streamers, each one contains "name", "description" and "url"    |
|            |                                           |            |                                                                         |


## Synapses example

### brains

Get a city by argument in order

```yaml
  - name: "twitchtv-who-is-streaming"
    signals:
      - order: "Who is streaming right now?"
      - order: "Who is playing right now?"
    neurons:
      - twitchtv:
          client_id: "{{twitch_client_id}}"
          limit: 55
          user: "{{twitch_username}}"
          file_template: "templates/twitchtv.j2"
```

### template

```jinja
{{number}} of your favorite players are streaming now:
{% for streamer in streamers %}
  {{streamer['name']}} streaming {{streamer['status']}}
{% endfor %}
```

see more example in the [sample directory](https://github.com/bacardi55/kalliope-wwtime/blob/master/samples/)


* [my posts about kalliope](http://bacardi55.org/kalliope.html)


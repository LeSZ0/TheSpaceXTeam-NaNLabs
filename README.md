# TheSpaceXTeam-NaNLabs

## Downloading
Download the .zip archive or use the git clone command:
`git clone git@github.com:LeSZ0/TheSpaceXTeam-NaNLabs.git`

## Installation
Go to the cloned directory and run the following command:
`docker-compose up --build`.
This command would build the project and install all the needed dependencies.

## Endpoint call
If you want to make an endpoint request to create a new task, you should make a POST request to
`http://0.0.0.0:8000/`. GET Method is not allowed.

### Request examples

- Bug Card
```
curl -d '{"description": "Bug Two", "type": "Bug"}' http://0.0.0.0:8000
```

- Task Card
```
curl -d '{"title": "Task 1", "category": "Maintanance", "type": "Task"}' http://0.0.0.0:8000
```

- Issue Card
```
curl -d '{"description": "Issue number 1", "title": "Issue 2", "type": "Issue"}' http://0.0.0.0:8000
```

## Visual Result
Finally you could see the visual results in the following url: https://trello.com/b/Z89XkNXi/the-spacex-team


#### However, you can use your own board, app_key and token for trello. But you'll need to set your custom values replacing each in the "envs.env" file and rebuild the container.

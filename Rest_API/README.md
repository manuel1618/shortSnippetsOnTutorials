# Device Registry Service

## Prerequisites

- Install [Docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)
  - How to build it: docker-compose build (if any file has changed (**important**!))
  - How to run it: docker-compose up -d (the -d lets the service continue to run in the background - important for webserver, I guess)
- Install flask-restful  (conda install -c conda-forge flask-restful)
- [Postman](https://www.postman.com/downloads/) (App for sending Request to the database for testing purposes )
- shelve (a database which is suited for this project)
- Video I followed: [Link](https://www.youtube.com/watch?v=4T5Gnrmzjak)
- This video is awful at the end - far too quick! :(

## Usage

All responses will have the form

```json
{
    "date": "Mixed type holding the content",
    "message" :  "Description of what happened"
}
```

Subsequent response definition will only detail the expected value of the data 'field'

### List all devides

**Definition**

`GET /devices`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier":"floor-lamp",
        "name":"Floor Lamp",
        "device_type":"switch",
        "controller_gateway":"191.1.0.2",
    }
    {
        "identifier":"samsung-tv",
        "name":"Samsung TV",
        "device_type":"tv",
        "controller_gateway":"191.1.0.9",
    }
]

```

### Registering a new device

**Definition**

`Post /devices`

**Arguments**

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a friendly name for this device
- `"device_type":string` the type of the device as understood by the client
- `"controller_gateway": string` the IP adress of the device's controller

If a device with the given identifier already exists, the existing device will be overwritten.

**Response**

- '201 created' on sucess

```json  
{
    "identifier":"samsung-tv",
    "name":"Samsung TV",
    "device_type":"tv",
    "controller_gateway":"191.1.0.9",
}
```

## Lookup device details

`GET /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
    "identifier":"samsung-tv",
    "name":"Samsung TV",
    "device_type":"tv",
    "controller_gateway":"191.1.0.9",
}
```

## Delete a device

**Definition**

`DELETE /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success

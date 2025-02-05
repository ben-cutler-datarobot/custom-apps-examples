This is an example dash app. It requires the resource `Internally run apps on the root path` to be true, and that's the only advanced setup. 

The execution environment I used was a basic python one which should ship with DR: [DataRobot] Python 3.12 Applications Base

The key thing to getting this working is having the Dash object constructed with a `requests_pathname_prefix` set to be /custom_applications/{id}/ . You do not want other paths, like `routes_pathname_prefix` to be set.

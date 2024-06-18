# twoAPIs

A simple example manifest that deploys two API apps to Cloud Foundry serving a protected JSON file using the Staticfile Buildpack.
In addition this example shows how to set network policies with with the internal app domain for container to container networking that works with any port.
Check and adapt the routes in the manifest before pushing.

**Usage:** `cf push`

Once the apps are running, simply curl the endpoint (failing as by default there is no connection between apps on the internal route).

**Test 1:** `curl -G https://customer-api.apps.01.cf.eu01.onstackit.cloud/add --data-urlencode "num1=10" --data-urlencode "num2=20"`

Then grant the missing network access and let the change propagate for approx. 10 seconds with the following command (default protocol is TCP and default port is 8080 for HTTP):

**Grant Network Access:** `cf add-network-policy customer-api backend-api`

Now test again the same endpoint from above or this one:

**Test 1:** `curl -G https://customer-api.apps.01.cf.eu01.onstackit.cloud/multiply --data-urlencode "num1=10" --data-urlencode "num2=20"`

[More Details about Container to Container Networking within Cloud Foudry](https://docs.cloudfoundry.org/concepts/understand-cf-networking.html)

**Good to know (from the link above): To utilize TLS capabilities, the client application can connect to port 61443 on the destination application over HTTPS. Traffic to application container port 61443 is proxied to application port 8080 inside of the container. So the app does not need to implement that. =)**

**Please Note: This is an example with python apps based on Flask, which should not be used in productive environments.**

# Cross-site Request Forgery
Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. It allows an attacker to partly circumvent the same origin policy, which is designed to prevent different websites from interfering with each other.

CSRF forces authenticated users to submit a request to a Web application against which they are currently authenticated. CSRF attacks exploit the trust a Web application has in an authenticated user. (Conversely, cross-site scripting (XSS) attacks exploit the trust a user has in a particular Web application). A CSRF attack exploits a vulnerability in a Web application if it cannot differentiate between a request generated by an individual user and a request generated by a user without their consent.

An attacker’s aim for carrying out a CSRF attack is to force the user to submit a state-changing request. Examples include:
* Submitting or deleting a record.
* Submitting a transaction.
* Purchasing a product.
* Changing a password.
* Sending a message.
  
Social engineering platforms are often used by attackers to launch a CSRF attack. This tricks the victim into clicking a URL that contains a maliciously crafted, unauthorized request for a particular Web application. The user’s browser then sends this maliciously crafted request to a targeted Web application. The request also includes any credentials related to the particular website (e.g., user session cookies). If the user is in an active session with a targeted Web application, the application treats this new request as an authorized request submitted by the user. Thus, the attacker succeeds in exploiting the Web application’s CSRF vulnerability.

## Prevention
The most popular method to prevent Cross-site Request Forgery is to use a challenge token that is associated with a particular user and that is sent as a hidden value in every state-changing form in the web app. These are called CSRF tokens. The token should be:

* Unpredictable with high entropy, as for session tokens in general.
* Tied to the user's session.
* Strictly validated in every case before the relevant action is executed.

These tokens are inserted within hidden parameters of HTML forms related to critical server-side operations and not stored within session cookies. The easiest way to add a non-predictable parameter is to use a secure hash function (e.g., SHA-2) to hash the user’s session ID. To ensure randomness, the tokens must be generated by a cryptographically secure random number generator. They are then sent to client browsers. The browser will verify the legitimacy of the end-user request using these tokens and reject the request if the CSRF token fails to match the test.

## Detection - 

If you were looking for incoming CSRF attacks, what would you look for? (TODO)

## Does CSRF bypass SOP?

Same Origin Policy (SOP) is a browser-level security control which dictates how a document or script served by one origin can interact with a resource from some other origin. Basically, it prevents scripts running under one origin to read data from another origin.

Cross-domain requests and form submissions are still permitted but reading data from another origin is not permitted. This means that if you are performing a CSRF attack on a vulnerable site which results in some server side state change (e.g. user creation, document deletion etc), the attack will be successful but you would not be able to read the response.

In short SOP only prevents reading data which was served from a different origin. It does not cover cross-domain form submissions which are used to carry out a CSRF attack.
# Wiredgrid

Proof of concept of using Selenium-Grid and Seleniumwire package to automate the screenshot of websites using a HTTP/HTTPS/SOCKS proxy.

## Overall requirements

- Selenium Grid: Allow multiple, parallel test over remote machines
- Selenium Chrome: Chrome image configured to handle 5 simultaneous, concurrent, headless sessions.
- Selenium Proxy: MITM Proxy by [Seleniumwire](https://github.com/wkeeling/selenium-wire/)

## Try it

1. Start containers using  `docker-compose up -d`
2. Add a custom proxy in `sample.py`.
3. Run sample script  `docker-compose exec selenium-proxy python /code/sample.py`

## Notes and improvements

- [ ] Upgrade to Selenium 4
- [ ] Upgrade to Seleniumwire 5

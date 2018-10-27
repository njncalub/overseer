# overseer

![Status](https://img.shields.io/badge/status-planning-red.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) [![PRs welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=round-square)](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github) [![Formatted by Prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://prettier.io/)

A helpful tool for managing web novel wikis.

This is a work in progress, if you find a mistake, please [file an issue](https://github.com/njncalub/wn-wiki-insights/issues). Thanks!

## Requirements

- [pipenv](https://github.com/pypa/pipenv)
- [npm](https://www.npmjs.com/)

## Installation

```bash
# Go to the project directory.
cd <project directory>

# Install the python requirements using pipenv.
pipenv install

# Install the UI requirements using npm.
npm install
```

## Scraping novel data

```bash
# First, update the settings of your spider using your favorite editor.
vim spiders/structured.py

# Run the scraper using pipenv.
pipenv run scrapy runspider spiders/structured.py -o output.json
```

## Starting the app

```bash
# Use npm to start a local parcel development server.
$ npm start dev
Server running at http://localhost:1234
✨  Built in 3.37s.
```

## Contributing

**Imposter syndrome disclaimer**: We want your help. No, really.

There may be a little voice inside your head that is telling you that you're not ready to be an open source contributor; that your skills aren't nearly good enough to contribute. What could you possibly offer a project like this one?

We assure you - the little voice in your head is wrong. If you can write code at all, you can contribute code to open source. Contributing to open source projects is a fantastic way to advance one's coding skills. Writing perfect code isn't the measure of a good developer (that would disqualify all of us!); it's trying to create something, making mistakes, and learning from those mistakes. That's how we all improve, and we are happy to help others learn.

Being an open source contributor doesn't just mean writing code, either. You can help out by writing documentation, tests, or even giving feedback about the project (and yes - that includes giving feedback about the contribution process). Some of these contributions may be the most valuable to the project as a whole, because you're coming to the project with fresh eyes, so you can see the errors and assumptions that seasoned contributors have glossed over.

## Licensing

[MIT](./LICENSE). Take, adapt, use. A link back to this repo is appreciated.

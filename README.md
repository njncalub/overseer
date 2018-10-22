# wn-wiki-helper

[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A helpful tool for managing web novel wikis.

This is a work in progress, if you find a mistake, please [file an issue](https://github.com/njncalub/wn-wiki-insights/issues). Thanks!

## MVP 1 - Check List

- [x] Create a spider that saves the scraped novel data to a JSON file.
- [ ] Add a utility function that can load the JSON file to the database.
- [ ] Create a basic site that lists all the chapters.
- [ ] Ability to search through chapter contents.
- [ ] Ability to edit/reformat chapters.

## MVP 2 - Checklist
- [ ] Add/edit Tags to the Chapter.
- [ ] Tags can be clicked and the Chapters list will be filtered.
- [ ] RegExp can be used in the search query for advanced filtering.
- [ ] Automatically extract pronouns (e.g. Character Names, Locations, Items, etc) from the chapters using NLTK.

## Requirements

- [pipenv](https://github.com/pypa/pipenv)

## Model Definitions

The app should accept the following format. Modify as needed.

```typescript
export interface Chapter {
  url: string;
  chapter: number;
  title: string;
  content: string;
}

export interface Novel {
  title: string;
  chapters: Chapter[];
}
```

## Installation

```bash
# Go to the project directory.
$ cd <project directory>

# Install requirements using pipenv.
$ pipenv install
```

## Running the scraper

```bash
# First, update the settings of your spider using your favorite editor.
$ ${FCEDIT:-${VISUAL:-${EDITOR:-vim}}} spiders/structured.py

# Run the scraper using pipenv.
$ pipenv run scrapy runspider spiders/structured.py -o output.json
```

## Contributing

**Imposter syndrome disclaimer**: We want your help. No, really.

There may be a little voice inside your head that is telling you that you're not ready to be an open source contributor; that your skills aren't nearly good enough to contribute. What could you possibly offer a project like this one?

We assure you - the little voice in your head is wrong. If you can write code at all, you can contribute code to open source. Contributing to open source projects is a fantastic way to advance one's coding skills. Writing perfect code isn't the measure of a good developer (that would disqualify all of us!); it's trying to create something, making mistakes, and learning from those mistakes. That's how we all improve, and we are happy to help others learn.

Being an open source contributor doesn't just mean writing code, either. You can help out by writing documentation, tests, or even giving feedback about the project (and yes - that includes giving feedback about the contribution process). Some of these contributions may be the most valuable to the project as a whole, because you're coming to the project with fresh eyes, so you can see the errors and assumptions that seasoned contributors have glossed over.

## Licensing

[MIT](./LICENSE). Take, adapt, use. A link back to this repo is appreciated.

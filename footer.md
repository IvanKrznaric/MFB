% This defines the footer of the site, and is not parsed as a regular "page"
% We point to it with the following in `myst.yml`:
% site:
% parts:
% footer: footer.md

% Here we use `grid` to add a basic grid structure to the HTML,
% but the formatting column sizes are defined manually in css/footer.css
% see the `grid-template-columns` line.
:::::{grid} 3 3 5 5
:class: outer-grid col-screen


::::{div}
# Useful links
- [Faculty of Economics and Business](https://www.efzg.unizg.hr/en)
- [Department of Mathematics](https://www.efzg.unizg.hr/katedre-29721/matematika/29783)
- [Merlin](https://moodle.srce.hr/)
::::

<!-- Prazan prostor-->
::::{div}
::::

<!-- Logo -->
::::{div}
```{image} ./slike/EFZG logo.jpg
:width: 400 px
```
::::
:::::
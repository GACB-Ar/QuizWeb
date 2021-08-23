const d = document;

export default function scrollSpy() {
  const $sections = d.querySelectorAll('section[data-scroll-spy]');

  const cb = entries => {
    // console.log('entries', entries);

    entries.forEach(entry => {
      // console.log('entry', entry);
      const id = entry.target.getAttribute('id');
      // console.log(id);
      if (entry.isIntersecting) {
        d.querySelector(`a[data-scroll-spy][href='#${id}']`).classList.add('active');
      } else {
        d.querySelector(`a[data-scroll-spy][href='#${id}']`).classList.remove('active');
      };
    });
  };

  const observer = new IntersectionObserver(cb, {
    //root // si la omitimos toma por defecto el document
    // rootMargin: '-250px'
    threshold: [.5, .75]
    //visible cuando está entre el 50% y el 75% del viewport
  });
  // console.log('observer', observer);

  $sections.forEach(el => observer.observe(el));
};
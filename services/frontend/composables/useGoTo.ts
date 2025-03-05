function waitForElement (selector: string, timeout = 2000) : Promise<Element> {
  return new Promise((resolve, reject) => {
    const startTime = Date.now();
    // eslint-disable-next-line prefer-const
    let observer: MutationObserver;

    function checkElement () {
      const element = document.querySelector(selector);

      if (element) {
        resolve(element);
        observer.disconnect(); // Stop observing DOM changes
      } else if (Date.now() - startTime >= timeout) {
        reject(new Error(`Timeout exceeded while waiting for element with selector '${selector}'`));
        observer.disconnect(); // Stop observing DOM changes
      }
    }

    observer = new MutationObserver(checkElement);
    observer.observe(document.body, { childList: true, subtree: true });

    checkElement(); // Check initially in case the element is already present
  });
}


export async function useGoTo (selector: string, props: {offset? :number} = {}): Promise<void> {
  console.log(selector);
  let element: Element;
  try {
    element = await waitForElement(selector);
  } catch {
    // element not found
    return;
  }
  const yOffset = props?.offset ?? -80;
  const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;

  window.scrollTo({ top: y, behavior: "smooth" });
}
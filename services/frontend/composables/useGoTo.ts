import { useRouter, useRoute } from "vue-router";
import { nextTick } from "vue";

export async function useGoTo(
  selector: string,
  props: { offset?: number } = {}
): Promise<void> {
  const router = useRouter();
  const route = useRoute();
  const yOffset = props?.offset ?? -150;

  const hash = selector.startsWith("#") ? selector : "";
  const basePath = route.path.split("#")[0];
  const targetPath = selector.startsWith("/") ? selector : basePath + hash;
  const [pathOnly, hashOnly] = targetPath.split("#");

  if (route.path !== pathOnly) {
    // Navigate to target page
    await router.push(pathOnly + (hashOnly ? `#${hashOnly}` : ""));
    await nextTick();

    if (hashOnly) {
      try {
        const element = await waitForElement(`#${hashOnly}`);
        scrollToElement(element, yOffset);
      } catch (err) {
        console.warn(err);
      }
    }
  } else {
    // Same page — scroll directly
    if (hashOnly || selector.startsWith("#")) {
      try {
        const element = await waitForElement(`#${hashOnly ?? selector}`);
        scrollToElement(element, yOffset);
      } catch (err) {
        console.warn(err);
      }
    }
  }
}

// Scroll to the element smoothly
function scrollToElement(element: Element, offset: number) {
  const y = element.getBoundingClientRect().top + window.pageYOffset + offset;
  window.scrollTo({ top: y, behavior: "smooth" });
}

// Wait for the element to exist
function waitForElement(selector: string, timeout = 2000): Promise<Element> {
  return new Promise((resolve, reject) => {
    const startTime = Date.now();
    let observer: MutationObserver;

    function checkElement() {
      const element = document.querySelector(selector);
      if (element) {
        observer.disconnect(); // Stop observing DOM changes
        resolve(element);
      } else if (Date.now() - startTime >= timeout) {
        observer.disconnect(); // Stop observing DOM changes
        reject(new Error(`Timeout exceeded while waiting for element '${selector}'`));
      }
    }

    observer = new MutationObserver(checkElement);
    observer.observe(document.body, { childList: true, subtree: true });

    checkElement(); // Initial check in case the element already exists
  });
}

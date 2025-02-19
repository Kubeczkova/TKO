import type { UseFetchOptions } from "nuxt/app";

export function useAPI<T>(
    endpoint: string,
    options?: UseFetchOptions<T>,
) {
    if (!endpoint.startsWith("/")) {
        endpoint = `/${endpoint}`
    }

    const cfg = useRuntimeConfig()

    const fullUrl = `${cfg.public.backendUrl}${endpoint}`

    return useFetch(
        fullUrl,
        {...options}
    )
}

import os
import re

sidebar_content = """            <!-- Sidebar -->
            <aside class="col-lg-4">
                <div class="sticky-top" style="top: 20px;">
                    <div class="card mb-4 overflow-hidden">
                        <div class="card-header bg-primary text-white py-3">
                            <h5 class="m-0">LATEST NEWS</h5>
                        </div>
                        <div class="list-group list-group-flush">
                            <a href="market-volatility.html" class="list-group-item list-group-item-action py-3">
                                <h6 class="mb-1">Market Volatility: Meridian Isotope Prices Surge</h6>
                                <small class="text-muted"><script>document.write(new Date(Date.now() - 2 * 60 * 60 * 1000).toLocaleString());</script></small>
                            </a>
                            <a href="new-treaty.html" class="list-group-item list-group-item-action py-3">
                                <h6 class="mb-1">New Treaty Signed in Oakhaven Summit</h6>
                                <small class="text-muted"><script>document.write(new Date(Date.now() - 5 * 60 * 60 * 1000).toLocaleString());</script></small>
                            </a>
                            <a href="coastal-storm.html" class="list-group-item list-group-item-action py-3">
                                <h6 class="mb-1">Coastal Storm Warning: Port Meridian on High Alert</h6>
                                <small class="text-muted"><script>document.write(new Date(Date.now() - 8 * 60 * 60 * 1000).toLocaleString());</script></small>
                            </a>
                            <a href="fmc-article.html" class="list-group-item list-group-item-action py-3">
                                <h6 class="mb-1">Free from who? The Free Meridian Cartel's meteoric rise</h6>
                                <small class="text-muted">March 18, 2026</small>
                            </a>
                            <a href="roberto-rodriguez-death.html" class="list-group-item list-group-item-action py-3">
                                <h6 class="mb-1">The Mysterious Death of Roberto Rodriguez</h6>
                                <small class="text-muted">February 7, 2026</small>
                            </a>
                            <a href="agricultural-exports.html" class="list-group-item list-group-item-action py-3">
                                <h6 class="mb-1">Executive Order Signed to Boost Agricultural Exports</h6>
                                <small class="text-muted">March 18, 2026</small>
                            </a>
                        </div>
                    </div>

                    <div class="card bg-warning text-dark p-4">
                        <h5 class="fw-bold">Newsletter Signup</h5>
                        <p>Get the latest investigative reports from SMP delivered to your inbox.</p>
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="Email Address">
                            <button class="btn btn-dark" type="button">Join</button>
                        </div>
                        <small>Strictly no-cartel tracking policy.</small>
                    </div>
                </div>
            </aside>"""

base_dir = r"c:\dev\sanmeridiangov\press"
files = [
    "fmc-article.html",
    "roberto-rodriguez-death.html",
    "agricultural-exports.html",
    "infrastructure-bill.html",
    "police-operation.html",
    "tax-extension.html"
]

for f in files:
    filepath = os.path.join(base_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # If it's fmc-article.html, replace the existing sidebar
    if f == "fmc-article.html":
        # we can replace everything from <!-- Sidebar --> to </aside>
        pattern = re.compile(r'<!-- Sidebar -->.+?</aside>', re.DOTALL)
        content = pattern.sub(sidebar_content, content)
    else:
        # For the others, they might have `<div class="col-lg-8 offset-lg-2">` which needs to be `<div class="col-lg-8">`
        # and then the sidebar appended before the closing `</div>` of the `.row`.
        # First check if the file has `offset-lg-2`:
        if 'offset-lg-2' in content:
            content = content.replace('col-lg-8 offset-lg-2', 'col-lg-8')
            # They should have an `</div>` (for col-lg-8) and then `</div>` (for row).
            # We look for something like:
            #             </div>
            #         </div>
            #     </main>
            # And inject sidebar content before the matching row </div>.
            
            # Since these files are somewhat consistent, we can do a regex to find </main> and string match backwards
            idx = content.rfind('</div>\n        </div>\n    </main>')
            if idx != -1:
                replacement_idx = idx + 6 # right after col-lg-8's </div>
                new_str = content[:replacement_idx] + "\n\n" + sidebar_content + content[replacement_idx:]
                content = new_str
            else:
                print(f"Warning: could not inject into {f}")

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")

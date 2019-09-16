<!-- #######  YAY, I AM THE SOURCE EDITOR! #########-->
<h1 style="color: #5e9ca0;">Demo Test Framework for ElasticSearch!</h1>
<h3><a href="https://www.elastic.co/products/elasticsearch" rel="nofollow">https://www.elastic.co/products/elasticsearch</a></h3>
<p>Elasticsearch is a distributed RESTful search engine built for the cloud.&nbsp;</p>
<p><a href="https://github.com/elastic/elasticsearch">Opensource: https://github.com/elastic/elasticsearch</a></p>
<blockquote>
<pre class="programlisting prettyprint lang-sh prettyprinted"><span class="pln">docker run </span><span class="pun">-</span><span class="pln">p </span><span class="lit">9200</span><span class="pun">:</span><span class="lit">9200</span> <span class="pun">-</span><span class="pln">p </span><span class="lit">9300</span><span class="pun">:</span><span class="lit">9300</span> <span class="pun">-</span><span class="pln">e </span><span class="str">"discovery.type=single-node"</span><span class="pln"> doc</span></pre>
</blockquote>
<h2 style="color: #2e6c80;">Test Framework Components:</h2>
<ul>
<li><strong>Scripting Language:</strong> Python</li>
<li><strong>Version</strong> : 3.6
<ul>
<li>Pip: Package management system used to install and manage software packages written in Python.</li>
<li>Version : pip3</li>
</ul>
</li>
<li><strong>Python Packages:</strong>
<ul>
<li>pytest</li>
<li>requests</li>
<li>jinja2</li>
<li>pyYaml</li>
</ul>
</li>
</ul>
<h2 style="color: #2e6c80;">Architecture Diagram:</h2>
<p><strong><img src="https://github.com/dprabhua/elastic_pytest/blob/master/images/Archi.png" alt="Architecture Diagram" width="500" height="380" />&nbsp;</strong></p>
<p>&nbsp;</p>
<p><strong>&nbsp;</strong></p>

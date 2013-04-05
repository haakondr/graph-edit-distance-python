import algorithm.knn
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
import os.path

class nlp_knn(algorithm.knn):
    def __init__(self, k, instances, recall, dist_fn):
        super(nlp_knn, self).__init__(k, instances, dist_fn,
                filtering_fn=self.retrieve_relevant)
        self.recall = recall
        
        self.schema = Schema(id=ID(stored=True), content=TEXT(stored=True))
        if not os.path.exists("index"):
            os.mkdir("index")
        self.index = create_in("index", self.schema)
        self.writer = self.index.writer()

        self.instance_dict = {}
        for instance in self.instances:
            self.writer.add_document(ID=unicode(instance['name']),
                    content=unicode(instance['original']))
            self.instance_dict[unicode(instance['name'])] = instance
        self.writer.commit()

    def retrieve_relevant(self, document):
        text = [graph['original'] for graph in document]
        rel_docs = []
        
        with self.index.searcher() as searcher:
            q = searcher.document_number(content=unicode(text))
            results = searcher.more_like(q, "content", top=self.recall, normalize=True)
            for hit in results:
                rel_docs.append(hit['ID'])                
        
#TODO: hent ut relevante graph objects her
        return [self.instance_dict[doc_id] for doc_id in rel_docs] 

#include "bst.h"
//got help from Samuel Davis

// ---------------------------------------
// Node class
// Default constructor
Node::Node() {
	this->left = nullptr;
	this->right = nullptr;
	this->parent = nullptr;
}
// Constructor
Node::Node(int in) {
	this->left = nullptr;
	this->right = nullptr;
	this->parent = nullptr;
	this->key = in;
}
// Destructor
Node::~Node() {
	
}

// Add parent 
void Node::add_parent(Node* in) {
	this->parent = in;
}
// Add to left of current node
void Node::add_left(Node* in) {
	this->left = in;
}
// Add to right of current node
void Node::add_right(Node* in) {
	this->right = in;
}

// Get key
int Node::get_key()
{
	return this->key;
}
// Get parent node
Node* Node::get_parent()
{
	return this->parent;
}
// Get left node
Node* Node::get_left()
{
	return this->left;
}
// Get right node
Node* Node::get_right()
{
	return this->right;
}
// Print the key to ostream to
// Do not change this
void Node::print_info(ostream& to)
{
	to << key << endl;
}
// ---------------------------------------


// ---------------------------------------
// BST class
// Walk the subtree from the given node
void BST::inorder_walk(Node* in, ostream& to)
{
	if(in == nullptr) {
		return;
	} else {
		inorder_walk(in->get_left(), to);
		in->print_info(to);
		inorder_walk(in->get_right(), to);
	}
}

void BST::Transplant(Node* u, Node* v) {
	if (u->get_parent() == nullptr) {
		//T.root = v
		this->root = v;
	} else {
		if (u == u->get_parent()->get_left()) {
			u->get_parent()->add_left(v);
		} else {
			u->get_parent()->add_right(v);
		}
	}
	if (v != nullptr) {
		v->add_parent(u->get_parent());
	}
}

// Constructor
BST::BST()
{
	this->root = nullptr;
}

void inorder_delete(Node* in) {
	if (in == nullptr) {
		return;
	} 
	inorder_delete(in->get_left());
	inorder_delete(in->get_right());
	delete in;
}

// Destructor
BST::~BST()
{
	inorder_delete(this->root);
}
// Insert a node to the subtree
void BST::insert_node(Node* in)
{
	if (tree_search(in->get_key())) {
		delete in;
		return;
	}	
	Node* r = this->root;
	Node* y = nullptr;

	while (r != nullptr) {
		y = r;
		if (in->get_key() < r->get_key()) {
			r = r->get_left();
		} else { 
			r = r->get_right();		
		}
		in->add_parent(y);
	}

	if (y == nullptr) {
		this->root = in;
	} else {
		if (in->get_key() < y->get_key()) {
			y->add_left(in);
		} else {
			y->add_right(in);
		}
	}
}

// Delete a node to the subtree
void BST::delete_node(Node* out)
{
	Node* o = out;
	

	if (o->get_left() == nullptr) {
		Transplant(o, o->get_right());
	} else if (o->get_right() == nullptr) {
		Transplant(o, o->get_left());
	} else {
		Node* y = get_succ(o);
		if(y->get_parent() != o) {
			Transplant(y, y->get_right());
			y->add_right(o->get_right());
			y->get_right()->add_parent(y);
		} 
		Transplant(o,y);
		y->add_left(o->get_left());
		y->get_left()->add_parent(y);

	}	
	delete o;
}


// minimum key in the BST
Node* BST::tree_min()
{
	return get_min(this->root);
}
// maximum key in the BST
Node* BST::tree_max()
{
	return get_max(this->root);
}
// Get the minimum node from the subtree of given node
Node* BST::get_min(Node* in)
{
	Node* r = in;
	while (r->get_left() != nullptr) {
		r = r->get_left();
	}
	return r;
}
// Get the maximum node from the subtree of given node
Node* BST::get_max(Node* in)
{
	Node* r = in;
	while (r->get_right() != nullptr) {
		r = r->get_right();
	}
	return r;
}
// Get successor of the given node
Node* BST::get_succ(Node* in)
{
	Node* curr = in;
	if (curr == nullptr) {
		return nullptr;
	}

	if (curr->get_right() != nullptr) {
		return get_min(curr->get_right());
	}

	Node* y = curr->get_parent();
	while (y != nullptr && curr == y->get_right()) {
		curr = y;
		y = y->get_parent();
	}	
	return y;
}
// Get predecessor of the given node
Node* BST::get_pred(Node* in)
{
	Node* curr = in;
	if (curr == nullptr) {
		return nullptr;
	}

	if (curr->get_left() != nullptr) {
		return get_max(curr->get_left());			
	}

	Node* y = curr->get_parent();
	while(y != nullptr && curr == y->get_left()) {
		curr = y;
		y = y->get_parent();
	}
	return y;	
}
// Walk the BST from min to max
void BST::walk(ostream& to)
{
	inorder_walk(this->root, to);
}

// Search the tree for a given key
Node* BST::tree_search(int search_key)
{
	Node* r = this->root;
	while (r != nullptr && search_key != r->get_key()) {
		if (search_key < r->get_key()) {
			r = r->get_left();
		} else {
			r = r->get_right();
		}
	}
	return r;
}
// ---------------------------------------

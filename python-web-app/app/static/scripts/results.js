var results = [{
	"id": 1,
	"adoptable_id": 1,
	"name": "Babycakes",
	"model": "Adoptable",
	"attribute": "this is the description with highlights when searching A"
}, {
	"id": 2,
	"breed_id": 1,
	"name": "Abyssian",
	"model": "Breed",
	"attribute": "this is the description with highlights when searching A"
}, {
	"id": 3,
	"org_id": 1,
	"name": "Adoption Shelter",
	"model": "Organization",
	"attribute": "this is the description with highlights when searching A"
}]

var Title = React.createClass({
	propTypes: {
		title: React.PropTypes.string
	},

	render: function() {
		return (
			<header><h2>{this.props.title}</h2></header>
			)
	}
})

var SearchResults = React.createClass({
	propTypes: {
		desc: React.PropTypes.string
	},

	getDefaultProps: function() {
		return {
			desc: 'No results from your search input.'
		}
	},

	getInitialState: function() {
		return {
			value: 1
		}
	},

	componentDidMount: function() {
		this.setState({
			value: this.state.value + 19
		});
	},

	render: function() {
		console.log(this.props.results);

		var model = "N/A"
		if (this.props.isModel) {
			model = (<Model desc={this.props.desc} />)
		}

		return (
			<div>
				<ul>
					{this.props.results.map((result) => {
						return <Result result={result} key={result.id}/>
					})}
                </ul>
            </div>
		)
	}
})

var Result = React.createClass({
	propTypes: {
		desc: React.PropTypes.string
	},
	render: function() {
		return (
			<li>
				<strong><a href={"/" + this.props.result.model.toLowerCase() + "s/" + this.props.result.id}>{this.props.result.name}</a></strong><br/>
				<em>{this.props.result.model}</em><br/>
				{this.props.result.attribute}
			</li>
		)
	}
})

ReactDOM.render(
	<SearchResults results={results} />,
	document.getElementById('search_results')
);

ReactDOM.render(
	<Title title="Search Results" />,
	document.getElementById('head')
);